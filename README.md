![photo_2024-03-28_10-22-45](https://github.com/Belyashik2K/TruckersMP/assets/126521808/b19a4f29-a2bf-4692-8de3-221dd166e42a)
# VisionCraft API
> Fully async python wrapper for [VisionCraft API](https://api.visioncraft.top/docs)

## Installing

    pip install VisionCraftAPI

## Features
* Fully async methods
* Important methods return Pydantic model as result for easier interaction with data
* Full exception handling
* Full [documentation](https://vision.b2k.tech/) is available

## Usage
```python
import asyncio

from VisionCraftAPI import VisionCraftClient

async def generate_xl_image(client: VisionCraftClient,
                            prompt: str,
                            model: str,
                            sampler: str) -> bytes:
    images = await client.generate_xl_image(
        prompt=prompt,
        model=model,
        sampler=sampler
    )
    
    print('Image generated! Saving to image.png...')
    with open('image.png', 'wb') as file:
        file.write(images)   

async def main():
    # Set your API key
    api_key = "YOUR_API_KEY"
    # Create a VisionCraftClient instance
    client = VisionCraftClient(api_key=api_key)
    
    # Get all SDXL models and samplers
    models = await client.get_xl_models()
    samplers = await client.get_xl_samplers()

    # Generate an image with the first model and sampler
    await generate_xl_image(client=client,
                            prompt='A beautiful sunset',
                            model=models[0],
                            sampler=samplers[0])
            
if __name__ == '__main__':
    asyncio.run(main())
```

## Docs
> Go to https://vision.b2k.tech/ for more information about SDK
