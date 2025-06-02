import asyncio
import random
import time
import json
from typing import List, Optional, Dict, Any, Union, AsyncGenerator, Tuple, Callable, Set
import os
import datetime

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse, FileResponse
from fastapi import WebSocket, WebSocketDisconnect
from pydantic import BaseModel

# 临时导入 lifespan，后续会进一步重构
from server import lifespan, MODEL_NAME, CHAT_COMPLETION_ID_PREFIX, logger, is_initializing, is_playwright_ready, is_browser_connected, is_page_ready, worker_task, request_queue, processing_lock, model_switching_lock, model_list_fetch_event, parsed_model_list, current_ai_studio_model_id, excluded_model_ids, page_params_cache, params_cache_lock, _process_request_refactored, cancel_queued_request, WebSocketConnectionManager, log_ws_manager, setup_server_logging, restore_original_streams, _handle_model_list_response, _initialize_page_logic, _close_page_logic, _handle_initial_model_state_and_storage, _set_model_from_page_display, load_excluded_models, save_error_snapshot, detect_and_extract_page_error, get_response_via_edit_button, get_response_via_copy_button, _wait_for_response_completion, use_helper_get_response, use_stream_response, clear_stream_queue, switch_ai_studio_model, DEFAULT_FALLBACK_MODEL_ID, AUTH_PROFILES_DIR, ACTIVE_AUTH_DIR, SAVED_AUTH_DIR, LOG_DIR, APP_LOG_FILE_PATH, PROXY_SERVER_ENV, STREAM_PROXY_SERVER_ENV, NO_PROXY_ENV, AUTO_SAVE_AUTH, AUTH_SAVE_TIMEOUT, PLAYWRIGHT_PROXY_SETTINGS, MODELS_ENDPOINT_URL_CONTAINS, RESPONSE_COMPLETION_TIMEOUT, INITIAL_WAIT_MS_BEFORE_POLLING, POLLING_INTERVAL, POLLING_INTERVAL_STREAM, SILENCE_TIMEOUT_MS, POST_SPINNER_CHECK_DELAY_MS, FINAL_STATE_CHECK_TIMEOUT_MS, POST_COMPLETION_BUFFER, CLEAR_CHAT_VERIFY_TIMEOUT_MS, CLEAR_CHAT_VERIFY_INTERVAL_MS, CLICK_TIMEOUT_MS, CLIPBOARD_READ_TIMEOUT_MS, PSEUDO_STREAM_DELAY, EDIT_MESSAGE_BUTTON_SELECTOR, MESSAGE_TEXTAREA_SELECTOR, FINISH_EDIT_BUTTON_SELECTOR, PROMPT_TEXTAREA_SELECTOR, INPUT_SELECTOR, INPUT_SELECTOR2, SUBMIT_BUTTON_SELECTOR, RESPONSE_CONTAINER_SELECTOR, RESPONSE_TEXT_SELECTOR, LOADING_SPINNER_SELECTOR, OVERLAY_SELECTOR, WAIT_FOR_ELEMENT_TIMEOUT_MS, ERROR_TOAST_SELECTOR, CLEAR_CHAT_BUTTON_SELECTOR, CLEAR_CHAT_CONFIRM_BUTTON_SELECTOR, MORE_OPTIONS_BUTTON_SELECTOR, COPY_MARKDOWN_BUTTON_SELECTOR, COPY_MARKDOWN_BUTTON_SELECTOR_ALT, MAX_OUTPUT_TOKENS_SELECTOR, STOP_SEQUENCE_INPUT_SELECTOR, MAT_CHIP_REMOVE_BUTTON_SELECTOR, TOP_P_INPUT_SELECTOR, TEMPERATURE_INPUT_SELECTOR, USER_INPUT_START_MARKER_SERVER, USER_INPUT_END_MARKER_SERVER, DEBUG_LOGS_ENABLED, TRACE_LOGS_ENABLED, AI_STUDIO_URL_PATTERN, EXCLUDED_MODELS_FILENAME, ClientDisconnectedError

# --- Pydantic Models ---
class FunctionCall(BaseModel):
    name: str
    arguments: str

class ToolCall(BaseModel):
    id: str
    type: str = "function"
    function: FunctionCall

class MessageContentItem(BaseModel):
    type: str
    text: Optional[str] = None

class Message(BaseModel):
    role: str
    content: Union[str, List[MessageContentItem], None] = None
    name: Optional[str] = None
    tool_calls: Optional[List[ToolCall]] = None
    tool_call_id: Optional[str] = None

class ChatCompletionRequest(BaseModel):
    messages: List[Message]
    model: Optional[str] = MODEL_NAME
    stream: Optional[bool] = False
    temperature: Optional[float] = None
    max_output_tokens: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    top_p: Optional[float] = None

# --- FastAPI App 定义 ---
app = FastAPI(
    title="AI Studio Proxy Server (集成模式)",
    description="通过 Playwright与 AI Studio 交互的代理服务器。",
    version="0.6.0-integrated",
    lifespan=lifespan
)