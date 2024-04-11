import base64

from json import loads
from typing import Optional

from .http_client import HTTPClient
from .models import (RateLimits,
                     MidjourneyTask,
                     MidjourneyResult,
                     LLMAnswer,
                     WhisperResult)

class VisionCraftClient(HTTPClient):
    """
    Client for interacting with the VisionCraft API.
    
    API Docs: https://docs.visioncraft.top/
    SDK Docs: https://vision.b2k.tech/
    
    :param api_key: Your VisionCraft API key (you can get it from https://t.me/VisionCraft_bot)
    """
    
    API_HOST = 'https://api.visioncraft.top'
    
    def __init__(self, 
                 api_key: str) -> None:
        super().__init__()
        self.__api_key = api_key
        
    @property
    def api_key(self) -> str:
        return self.__api_key
    
    async def __get(self, 
                  url: str) -> dict | str | list:
        return await self._request(method="GET",
                                   url=url)

    async def __post(self,
                   url: str,
                   **kwargs) -> dict | str | list:
        return await self._request(method="POST",
                                   url=url,
                                   **kwargs)
    
    async def get_models(self) -> list:
        """
        Get list of all StableDiffusion 1.x models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-1.x-models/available-models
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-1.x-models/get_models
        
        :return: A list of StableDiffusion 1.x models
        """
        return await self.__get(f'{self.API_HOST}/models')
    
    async def get_xl_models(self) -> list:
        """
        Get list of all StableDiffusion XL models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-xl-models/available-models
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-xl-models/get_xl_models
        
        :return: A list of StableDiffusion XL models
        """
        return await self.__get(f'{self.API_HOST}/models-xl')
    
    async def get_llm_models(self) -> list:
        """
        Get list of all LLM models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/llm-models/available-models
        SDK Docs: https://vision.b2k.tech/docs/api-methods/large-language-models-llms/get_llm_models
        
        :return: A list of LLM models
        """
        return await self.__get(f'{self.API_HOST}/models-llm')
    
    async def get_upscale_models(self) -> list:
        """
        Get list of all upscale models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/image-upscale/available-models
        SDK Docs: https://vision.b2k.tech/docs/api-methods/image-upscale/get_upscale_models
        
        :return: A list of upscale models
        """
        return await self.__get(f'{self.API_HOST}/models-upscale')

    async def get_samplers(self) -> list:
        """
        Get list of all samplers for StableDiffusion 1.x models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-1.x-models/available-samplers
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-1.x-models/get_samplers
        
        :return: A list of samplers for StableDiffusion 1.x models
        """
        return await self.__get(f'{self.API_HOST}/samplers')
    
    async def get_xl_samplers(self) -> list:
        """
        Get list of all samplers for StableDiffusion XL models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-xl-models/available-samplers
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-xl-models/get_xl_samplers
        
        :return: A list of samplers for StableDiffusion XL models
        """
        return await self.__get(f'{self.API_HOST}/samplers-xl')
        
    async def get_loras(self) -> list:
        """
        Get list of all LORAs for StableDiffusion 1.x models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-1.x-models/available-loras
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-1.x-models/get_loras
        
        :return: A list of LORAs for StableDiffusion 1.x models
        """
        return await self.__get(f'{self.API_HOST}/loras')
    
    async def get_limits(self) -> RateLimits:
        """
        Get info about rate limits for free users.
        
        API Docs: https://api.visioncraft.top/limits
        SDK Docs: https://vision.b2k.tech/docs/api-methods/api-limits/get_limits
        
        :return: A RateLimits object
        """
        
        limits: dict = loads(await self.__get(f'{self.API_HOST}/limits'))
        
        new_keys = {
            "SD 1.X": "STABLEDIFFUSION",
            "SDXL models": "STABLEDIFFUSIONXL",
            "DALLE-3": "DALLE3",
            "Image Upscalilng": "IMAGEUPSCALING"
        }
        
        for key, _ in limits.copy().items():
            if key in ["SD 1.X", "SDXL models", "DALLE-3", "Image Upscalilng"]:
                limits[new_keys[key]] = limits[key]
            else:
                limits[key.upper()] = limits[key]
                
            if key != key.upper():
                del limits[key]
        return RateLimits(**limits)
    
    async def get_i2i_schedulers(self) -> list:
        """
        Get list of all schedulers for Image2Image model.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/image2image/available-schedulers
        SDK Docs: https://vision.b2k.tech/docs/api-methods/image2image/get_i2i_schedulers
        
        :return: A list of schedulers for Image2Image model
        """
        return await self.__get(f'{self.API_HOST}/img2img/schedulers')
    
    async def get_i2i_refiners(self) -> list:
        """
        Get list of all refiners for Image2Image model.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/image2image/available-refiners
        SDK Docs: https://vision.b2k.tech/docs/api-methods/image2image/get_i2i_refiners
        
        :return: A list of refiners for Image2Image model
        """
        return await self.__get(f'{self.API_HOST}/img2img/refiners')
    
    async def generate_image(self,
                             prompt: str,
                             model: str,
                             sampler: str,
                             width: Optional[int] = 1024,
                             height: Optional[int] = 1024,
                             image_count: Optional[int] = 1,
                             negative_prompt: Optional[str] = str(),
                             cfg_scale: Optional[int] = 10,
                             steps: Optional[int] = 30,
                             loras: Optional[dict] = {},
                             upscale: Optional[bool] = False) -> list[str]:
        """
        Generate an image using StableDiffusion 1.x models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-1.x-models/image-generation
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-1.x-models/generate_image
        
        :param prompt: A text prompt for image generation
        :param model: A StableDiffusion 1.x model from the list of available models
        :param sampler: A sampler from the list of available samplers
        :param width: Width of the generated image (min: 512, max: 1024, default: 1024)
        :param height: Height of the generated image (min: 512, max: 1024, default: 1024)
        :param image_count: Number of images to generate (max: 5, default: 1)
        :param negative_prompt: A negative text prompt for image generation
        :param cfg_scale: A scale for the configuration (min: 1, max: 20, default: 10)
        :param steps: Number of steps for image generation (min: 1, max: 30, default: 30)
        :param loras: A dictionary of LORAs for the model
        :param upscale: Whether to upscale the image or not
        
        :return: A list of image URLs  
        """
        json = {
            "model": model,
            "sampler": sampler,
            "prompt": prompt,
            "width": width,
            "height": height,
            "negative_prompt": negative_prompt,
            "image_count": image_count,
            "token": self.api_key,
            "cfg_scale": cfg_scale,
            "steps": steps,
            "loras": loras,
            "upscale": upscale
        }
        
        result = await self.__post(f'{self.API_HOST}/generate', json=json)
        return result["images"]
    
    async def generate_xl_image(self,
                                prompt: str,
                                model: str,
                                sampler: str,
                                width: Optional[int] = 1024,
                                height: Optional[int] = 1024,
                                negative_prompt: Optional[str] = str(),
                                cfg_scale: Optional[int] = 10,
                                steps: Optional[int] = 30,
                                image_count: Optional[int] = 1) -> list[str]:
        """
        Generate an image using StableDiffusion XL models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/stablediffusion-xl-models/image-generation
        SDK Docs: https://vision.b2k.tech/docs/api-methods/stablediffusion-xl-models/generate_xl_image
        
        :param prompt: A text prompt for image generation
        :param model: A StableDiffusion XL model from the list of available models
        :param sampler: A sampler from the list of available samplers
        :param width: Width of the generated image (min: 512, max: 1024, default: 1024)
        :param height: Height of the generated image (min: 512, max: 1024, default: 1024)
        :param negative_prompt: A negative text prompt for image generation
        :param cfg_scale: A scale for the configuration (min: 1, max: 20, default: 10)
        :param steps: Number of steps for image generation (min: 1, max: 30, default: 30)
        :param image_count: Number of images to generate (max: 5, default: 1)
        
        :return: A list of image URLs
        """
        
        json = {
            "prompt": prompt,
            "model": model,
            "negative_prompt": negative_prompt,
            "token": self.api_key,
            "height": height,
            "width": width,
            "sampler": sampler,
            "cfg_scale": cfg_scale,
            "steps": steps,
            "image_count": image_count
        }
        
        result = await self.__post(f'{self.API_HOST}/generate-xl', json=json)
        return result['images']
        
    async def create_midjourney_task(self,
                                     prompt: str) -> MidjourneyTask:
        """
        Create a Midjourney image generation task.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/midjourney/create-task
        SDK Docs: https://vision.b2k.tech/docs/api-methods/midjourney/create_midjourney_task
        
        :param prompt: A text prompt for image generation
        
        :return: A MidjourneyTask object
        """
        
        json = {
            "prompt": prompt,
            "token": self.api_key
        }
        
        result = await self.__post(f'{self.API_HOST}/midjourney', json=json)
        return MidjourneyTask(**result)
    
    async def get_midjourney_task(self,
                                  task_id: int) -> MidjourneyResult:
        """
        Get the result of a Midjourney image generation task.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/midjourney/get-image-status-by-taskid
        SDK Docs: https://vision.b2k.tech/docs/api-methods/midjourney/get_midjourney_task
        
        :param task_id: The ID of the task
        
        :return: A MidjourneyResult object
        """
        
        json = {
            "task_id": str(task_id),
            "token": self.api_key
        }
        
        result = await self.__post(f'{self.API_HOST}/midjourney/result', json=json)
        return MidjourneyResult(**result)
    
    async def image_upscaling(self,
                              image: str | bytes,
                              model: str,
                              resize: Optional[int] = 2) -> bytes:     
        """
        Upscale an image.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/image-upscale/upscale
        SDK Docs: https://vision.b2k.tech/docs/api-methods/image-upscale/image_upscaling
        
        :param image: A URL or bytes object of the image to upscale
        :param model: An upscale model from the list of available models
        :param resize: How many times to improve a photo (2 or 4)
        
        :return: A bytes object of the upscaled image
        """   
        
        if type(image) == bytes:
            image = base64.b64encode(image).decode('utf-8')
        
        json = {
            "image": image,
            "token": self.api_key,
            "model": model,
            "resize": resize
        }
        
        return await self.__post(f'{self.API_HOST}/upscale', json=json)
    
    async def image2image(self,
                          image: str | bytes,
                          prompt: str,
                          scheduler: str,
                          refiner: str,
                          mask: Optional[str] = str(),
                          negative_prompt: Optional[str] = str(),
                          steps: Optional[int] = 50,
                          strength: Optional[float] = 0.8) -> bytes:
        """
        Generate an image using Image2Image models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/image2image/generation
        SDK Docs: https://vision.b2k.tech/docs/api-methods/image2image/image2image
        
        :param image: A URL or bytes object of the image to generate
        :param prompt: A text prompt for image generation
        :param scheduler: A scheduler from the list of available schedulers
        :param refiner: A refiner from the list of available refiners
        :param mask: A mask for the image
        :param negative_prompt: A negative text prompt for image generation
        :param steps: Number of steps for image generation (min: 1, max: 50, default: 50)
        :param strength: Strength of the image generation (min: 0.1, max: 1.0, default: 0.8)
        
        :return: A bytes object of the generated image
        """
        
        if type(image) == bytes:
            image = base64.b64encode(image).decode('utf-8')
        
        json = {
            "image": image,
            "prompt": prompt,
            "scheduler": scheduler,
            "refiner": refiner,
            "mask": mask,
            "negative_prompt": negative_prompt,
            "steps": steps,
            "strength": strength,
            "token": self.api_key
        }
        
        return await self.__post(f'{self.API_HOST}/img2img', json=json)
    
    async def generate_gif(self,
                           prompt: str,
                           sampler: str,
                           negative_prompt: Optional[str] = str(),
                           cfg_scale: Optional[int] = 10,
                           steps: Optional[int] = 30) -> str:
        """
        Generate a GIF by text prompt.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/text2gif/gif-generation
        SDK Docs: https://vision.b2k.tech/docs/api-methods/text2gif/generate_gif
        
        :param prompt: A text prompt for GIF generation
        :param sampler: A sampler from the list of available samplers
        :param negative_prompt: A negative text prompt for GIF generation
        :param cfg_scale: A scale for the configuration (min: 1, max: 20, default: 10)
        :param steps: Number of steps for GIF generation (min: 1, max: 50, default: 30)
        
        :return: A URL of the generated GIF
        """
        json = {
            "prompt": prompt,
            "sampler": sampler,
            "negative_prompt": negative_prompt,
            "cfg_scale": cfg_scale,
            "steps": steps,
            "token": self.api_key
        }
        
        result = await self.__post(f'{self.API_HOST}/generate-gif', json=json)
        return result['images'][0]
    
    async def llm_chatting(self,
                           model: str,
                           messages: list[dict],
                           max_tokens: Optional[int] = 4096,
                           temperature: Optional[float] = 0.7,
                           top_p: Optional[float] = 0.9,
                           top_k: Optional[int] = 0,
                           repetition_penalty: Optional[int] = 1,
                           presence_penalty: Optional[int] = 0,
                           frequency_penalty: Optional[int] = 0,) -> LLMAnswer:
        """
        Chat with LLM models.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/llm-models/text-generation
        SDK Docs: https://vision.b2k.tech/docs/api-methods/large-language-models-llms/llm_chatting
        
        :param model: An LLM model from the list of available models
        :param messages: A list of messages for chatting
        :param max_tokens: Maximum length of the newly generated generated text (min: 128, max: 100000, default: 512)
        :param temperature: Temperature for sampling (min: 0, max: 100, default: 0.7)
        :param top_p: Top-p for nucleus sampling (min: 0, max: 1, default: 0.9)
        :param top_k: Top-k for nucleus sampling (min: 0, max: 99999, default: 0)
        :param repetition_penalty: Repetition penalty for sampling (min: 0.01, max: 5, default: 1)
        :param presence_penalty: Presence penalty for sampling (min: -2, max: 2, default: 0)
        :param frequency_penalty: Frequency penalty for sampling (min: -2, max: 2, default: 0)
        
        :return: A LLMAnswer object
        """
                    
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }  
    
        data = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "repetition_penalty": repetition_penalty,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "token": self.api_key
        }
        
        result = await self.__post(f'{self.API_HOST}/v1/chat/completions',
                                   headers=headers,
                                   json=data)
        return LLMAnswer(**result['choices'][0]['message'])
    
    async def whisper(self,
                      audio: str | bytes,
                      task: str,
                      language: Optional[str] = 'auto') -> WhisperResult:
        """
        Transcribe or translate an audio to text using Whisper model.
        
        API Docs: https://docs.visioncraft.top/interacting-with-the-api/whisper/audio-transcription-or-translation
        SDK Docs: https://vision.b2k.tech/docs/api-methods/whisper/whisper
        
        :param audio: A URL or bytes object of the audio to transcribe or translate
        :param task: A task to perform (transcribe or translate)
        :param language: An audio language in ISO 639-1 format (default: auto)
        
        :return: A WhisperResult object
        """
        if type(audio) == bytes:
            audio = base64.b64encode(audio).decode("utf-8")
        
        json = {
            "audio": audio,
            "task": task,
            "language": language,
            "token": self.api_key
        }
        
        result = await self.__post(f'{self.API_HOST}/whisper', json=json)
        return WhisperResult(**result)