# RecycleNet 
## Inspiration
RecycleNet is a project inspired by the growing magnitude of the global waste problem. 
Though reducing our overall footprint should be our final goal, increasing efficiency of recycling will help curb the problem.
Though most countries have begun recycling programs, it is limited to splitting waste in two groups : recyclable and non-recyclable. 
Splitting the recyclable waste into the different groups that require seperate processes is a time a labour intensive process. 
Another issue is the lack of awareness among people on the correct way to split and prepare waste.

By using Computer vision, both these problems can be solved. 

# V2
## Implementation
V2 of RecycleNet, I decided to move to an object detection model for increased fucntionality. Yolov5 architecture was chosen for it's accuracy and inference speed. Data was obtained from https://www.kaggle.com/arkadiyhacks/drinking-waste-classification/version/2

## Performance
Overall acheived accuracy of over 95%. Results can be seen below.
# V1
## Implementation
This Nerual network was implented using Transfer learning on the VGG16 model. Data was obtained from https://github.com/garythung/trashnet/tree/master/data 

Next, the model and API were hosted using Flask on a AWS EC2 instance for easy access.

## Performance
Overall acheived accuracy of over 85%.

## Next Steps
The next step would be to build a mobile app that can access the API to help users determine which category their waste belongs to, and how best to prepare it for recycling 
