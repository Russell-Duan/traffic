# App Tutorial

This WebApp displays the traffic density of the LA county on its first page as shown below.

![png](/data/pic_1.png)

According to the graph, you will interpret the traffic density of LA which the darker the area means the higher traffic density. By moving the mouse, you are able to see the area ID of each area which is useful for further functionality.

![png](/data/pic_2.png)

By selecting the from and to address, day of week, and hour of day, one can click "Submit form" and the page will return the shortest path and time estimation like below.

![png](/data/pic_3.png)

## Possible Limitations

Even though my WebApp could return the shortest path and the time estimation, my time estimation model is relatively simple and it is not accurate for long distance. Therefore, the time estimation model has lots of space to improve, and it is one of the largest limitation of my app. Besides the time estimation model, my app only accepts area ID but not street names because the data source didn't provide me the street names. In future, I would like to add street names to the map to make it more accessible.

## Workflow

Since the ipynb is too large to be uploaded to Github, I have made my workflow into a blog post at [here](https://russell-duan.github.io/project-workflow/). It shows how the graphs are constructed and plotted, and also shows the workflow to derive the shortest path and the time estimation.

## Instructions

Since this project includes large dataset, I failed to deploy the WebApp to Heroku. In order to interact with my WebApp, you will have to clone the repository and run the "app.py" to view the app locally. It is OK to run "app.py" directly because I have added `app.run()` at the end of the file. When testing the functionality of the shortest path and the time estimation for the first time, it may take up to 5 minutes to download the dataset from Google Drive which has a size of 1.2GB. Once the initialization is done, you can test the functions really quick.