# txt_to_excel
Parse and write chipset test output file to excel 

## Usage 
````
usage: run.py [-h] --tool convert, rename
              [--source_dir source-directory/TextFile]
              [--target_dir target-directory/ExcelFile]
````

### Example

command to convert txt file to excel file
````
python run.py --tool convert --source_dir G:\ChipOutput --target_dir C:\ExcelFiles 
````
command to bulk rename file in source directory
````
python run.py --tool rename --source_dir G:\TextFiles 
````
