![photo (4)](https://github.com/Belyashik2K/VisionCraftAPI/assets/126521808/fa32e4fa-37bd-47a7-9574-bbc02191796b)
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
import aiohttp

from VisionCraftAPI import VisionCraftClient

async def generate_xl_image(client: VisionCraftClient,
                            prompt: str,
                            model: str,
                            sampler: str,
                            image_count: int):
    images = await client.generate_xl_image(
        prompt=prompt,
        model=model,
        sampler=sampler,
        image_count=image_count
    )
    
    print('Images generated! Saving it...')
    # Download and save the generated images
    async with aiohttp.ClientSession() as session:
        for i, image_url in enumerate(images):
            async with session.get(image_url) as image_response:
                image_data = await image_response.read()
                # Save the image locally
                with open(f"generated_image_{i}.png", "wb") as f:
                    f.write(image_data)
                    
async def main():
    # Set your API key
    api_key = "54bdfe91-eb76-47c0-a156-6fc9dd2f7db2"
    # Create a VisionCraftClient instance
    client = VisionCraftClient(api_key=api_key)
    
    # Get all SDXL models and samplers
    models = await client.get_xl_models()
    samplers = await client.get_xl_samplers()

    # Generate an image with the first model and sampler
    await generate_xl_image(client=client,
                            prompt='A beautiful sunset',
                            model=models[0],
                            sampler=samplers[0],
                            image_count=4)
            
if __name__ == '__main__':
    asyncio.run(main())
```

## Docs
> Go to https://vision.b2k.tech/ for more information about SDK
