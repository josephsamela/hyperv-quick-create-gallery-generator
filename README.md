# Hyper-V Quick Create Gallery Generator
Hyper-V Quick Create is great - but making that `.json` gallery is a massive pain! Here's a python script to generate that file for you!

## How to use

Organize your gallery like this:

```
gallery
	└─ Image Name
		├─ description.txt
		├─ version.txt
		├─ details.json
		├─ logo.png
		├─ symbol.png
		├─ thumbnail.png
		└─ disk.vhdx
```

> `gallery` Root directory of containing image folders
>
> 
>
> `Image Name` Name of image in Gallery
>
> 
>
> `discription.txt` Paragraph of text describing contents/purpose of image
>
> 
>
> `version.txt` Image version number
>
> 
>
> `details.json` json array of key/value pairs containing image details
>
> 
>
> `logo.png` Company logo displayed on under thumbnail on gallery page
>
> 
>
> `symbol.png` Symbol displayed in gallery image list
>
> 
>
> `thumbnail.png` Thumbnail of desktop displayed on gallery page
>
> 
>
> `disk.vhdx` The virtual machine .vhd or .vhdx disk image



Run `generate_new_gallery.py` and let it go!

```python
$ python generate_new_gallery.py
```

The Quick Create gallery requires SHA256 hash of each file. If you have 10GB+ disk images this can take a while...go grab some coffee and watch console progress.

## Example

Included in this repo is an example to show how to build you gallery. Remember you need to add the path to `gallery.json` to registry `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization`.