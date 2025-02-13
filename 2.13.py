from pandas import read_csv
def create_tag_mapping(mapping_csv):
    labels = set()
    for i in range(len(mapping_csv)):
        tags = mapping_csv['tags'][i].split(' ')
        labels.update(tags)
    labels = list(labels)
    labels.sort()
    labels_map = {labels[i]:i for i in range(len(labels))}
    inv_labels_map = {i:labels[i] for i in range(len(labels))}
    return labels_map, inv_labels_map
filename = 'train_v2.csv'
mapping_csv = read_csv(filename)
mapping, inv_mapping = create_tag_mapping(mapping_csv)
print(len(mapping))
print(mapping)