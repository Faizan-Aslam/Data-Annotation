import fiftyone as fo
import fiftyone.zoo as foz

dataset_path = r'C:/Users/faiza/Documents/Annot/WP4/4a/colour'

labels_path = r'C:/Users/faiza/Documents/Annot/annotations_4a.json'

# Import the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=dataset_path,
    labels_path=labels_path,
)

session = fo.launch_app(dataset, port=5151)

# dataset = foz.load_zoo_dataset("quickstart")
# session = fo.launch_app(dataset)