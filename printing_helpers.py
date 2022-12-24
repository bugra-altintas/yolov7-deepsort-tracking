

def print_results(results):
    for key in results:
        print("Bee",key,":")
        for p in results[key]:
            print("\t",p)

def draw_tracking_lines(results,videopath):
    centers = get_centers(id,results)


# calculate centers of bounding boxes
def get_centers(id,results):
    centers = []
    for box in results[id]:
        centers.append([box[0],(box[2] + box[4])/2,(box[3] + box[5])/2])
    return centers