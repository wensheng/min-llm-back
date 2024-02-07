from typing import List, Optional
from pydantic import BaseModel


class OAIMessage(BaseModel):
    role: str = 'assistant'
    content: str


class OAIChatCompletionRequest(BaseModel):
    model: str
    messages: List[OAIMessage]
    temperature: Optional[float] = 0.8
    top_p: Optional[float] = 0.95
    min_p: Optional[float] = 0.05
    top_k: Optional[int] = 40
    repeat_penalty: Optional[float] = 0
    stream: Optional[bool] = True


class OAIChoice(BaseModel):
    index: int
    message: OAIMessage
    logprobs: Optional[str] = None
    finish_reason: str = 'stop'


class OAIUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class OAIChatCompletionResponse(BaseModel):
    id: str
    object: 'chat.completion'
    created: int
    model: str
    choices: list[OAIChoice]
    usage: OAIUsage


class OAIError(BaseModel):
    message: str
    type: str
    param: Optional[str] = None
    code: str


class OAIErrorResponse(BaseModel):
    error: OAIError
