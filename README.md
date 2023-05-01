# Bioassay Well Plate

by Megan Tran

## Table of Contents
* [Purpose of Program](#Purpose-of-program)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to Use the Program](#How-to-Use-the-Program)

## Purpose of Program

I created this spreadsheet to mimic the layout of a 96- well plate for the Baker Research Group, a lab I am an undergraduate research assistant for. This program allows members of the lab to fill out what wells of the plate they put their sample in, which lets others know whose sample is where before sending the plate off for bioassay. 

When coding this program, a challenge I faced was figuring out how to embed the drop-down list into the spreadsheet. I could make the dropdown box outside of the spreadsheet, but not how I wanted it to function. Another challenge I faced was attempting to change the labels of the rows of the spreadsheet to letters instead of numbers. 

Some features I hope to implement in this program is that the user can color code their selection on the spreadsheet and something that allows the user to enter their sample name along with their name.

## Technologies

Languages/Enviroments used

Jupyter Notebook 6.5.2

Python 3.10.9

## Setup

Install Jupyter Notebook with
> https://jupyter.org/install

type
```
pip install notebook 
```
and to run the notebook type
```
jupyter notebook
```
## How to Use the Program

Below is the image of the spreadsheet that is modelled similar to the structure of a well- plate:
<img width="743" alt="image" src="https://user-images.githubusercontent.com/68253811/235381449-2b75d716-6f6f-4909-94af-e3e5729bcea4.png">
Simply click on any cell to bring down a list of names and choose the name of your choice to fill in a spot on the well-plate.

The run interact button brings up a diagram of a sample 96 well-plate for reference.
![ezgif com-video-to-gif](https://user-images.githubusercontent.com/68253811/235382342-ebbf2cac-7c72-4851-ac7b-a83489a370fa.gif)
### Credits
I referred to the links below to create my spreadsheet and the widgets:

Thanks to Ryan Noonam for providing introductions on how to set up a spreadsheet on Jupyter Notebook
> https://youtu.be/fKKtO1w77bg
> https://www.youtube.com/watch?v=HY7cf-CYs1o


Thanks to Maxivellz for providing the code for embedding the dropdown menu into the spreadsheet.
> https://stackoverflow.com/questions/72942721/how-to-embed-a-dropdown-ipywidget-in-an-ipysheet-spreadsheet
