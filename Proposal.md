### Abstract

My project visualizes the traffic density of Los Angeles, which simply means how the traffic is in the city of Los Angeles at anytime. Besides the visualization, I will implement several functions that will display the shortest path with the estimated time going from A to B at anytime you specified. I will mainly use Scrapy to get traffic data, Plotly and Networkx to do the visualization and to implement the functions needed.

### Planned Deliverables

I'm aiming to create an local app that able to show the map with traffic density, the shortest path with time estimation based on the user's input.

If everything works out exactly as I planned, the app will ask the user whether they want map or the shortest path with estimation and automatically prints out the result without throwing errors. It shall have the local app interface.

If it doesn't 100% workout, I still expect the visualizations with different time frame to be showed.

### Resources Required

I will use a public data source provided by Uber to download the traffic data of the city of Los Angeles. Besids the traffic data, I might also use the map data provided by the LA County eGIS Program. The link for Uber's data is [here](https://movement.uber.com/?lang=en-US), and the link for eGIS's data is [here](https://egis-lacounty.hub.arcgis.com/).

### Tools and Skills Required

The skills that I will be needing is database management, modeling, complex visualizaiton, network analysis. I need `sqlite3` to handle the large traffic data sets and map data sets, and I also need some preprocessings with `pandas` so that I can combine the two data sets into one. I can perform the modeling process which effectively computes the traffic density either by using `numpy` or `TensorFlow`. For the visualization, `Plotly` is my first choice because of its interactive feature. Finally, I will do the network analysis with `NetworkX` which is able to compute many useful features.

### What You Will Learn

By completing this project, I will be more familiar with `Plotly` and `NetworkX` while having a sense of what network data science looks like and what it is capable of doing. Besides the specific tools in Python, I'd like to learn the version control with Github which forces me to design my project before coding.

### Risks

The first thing that could stop me is that the two data sets may have different borders on each district. Even though I don't expect any large differences, but I do know there will be little variations that I have to take care of when cleaning the data.

The second thing that could stop me is the user interface design. As I invested most of my time on data science with python, I'm not very familiar with any tools related to the front end development. To be more prepared for the user interface design, I might need to learn `Streamlit` or `Tkinter`.

### Ethics

People who commute mainly by cars or buses have the potential to be benefited from the existence of our product. Imagine that you are going to take a GRE test on a test center that you have never been before, you have to know how long it takes to get there from the place you live. One can do that by searching the route on Google Maps immidiately, but one couldn't know the actual time that it will take on the day of the exam. With the existence of our product, one could be more prepared and more confident on the test day.
However, the skilled drivers or the citizens who have lived in the neighborhood for decades might be harmed. As our product will return the shortest path, the shortcuts will be known for many others which will make the shortcuts no longer shortcuts and affects the drivers who get used to those shortcuts.

The world will definitely become a better place because of the existence of our product. If my product makes it easier for people to know the traffic of the city of Los Angeles at anytime, my first assumption is that the traffic density on each weekday is differed from another, but it is similar to the same weekday in other weeks. Therefore, the world is a better place as people stop being bothered with the unexpected traffic jams (although they will still be bothered sometimes because car accidents are still going to happen and destroy the traffic flow).

### Tentative Timeline
After two weeks: Download and preprocess the two data sets. Modeling the traffic density.

After four weeks: Use the modeled data to make plots and to construct the network.

After six weeks: Implement the functions needed and design the user interface.