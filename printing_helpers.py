import cv2 as cv

def print_results(results):
    for key in results:
        print("Bee",key,":")
        for p in results[key]:
            print("\t",p)

def print_frame_data(frame_data):
    for i,frame in enumerate(frame_data):
        print("Frame",i+1,":")
        for p in frame:
            print("\t",p)

def draw_tracking_lines(results,bee_id,videopath,output_path):
    # read video
    vid = cv.VideoCapture(videopath)
    # get video ready to save locally if flag is set
    width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))  # by default VideoCapture returns float instead of int
    height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(vid.get(cv.CAP_PROP_FPS))
    codec = cv.VideoWriter_fourcc(*"XVID")
    out = cv.VideoWriter(output_path, codec, fps, (width, height))
    # initialize the results dict
    
    positions = results[bee_id]
    lines = []

    for i in range(1,len(positions)-1):
        pt1 = ((positions[i-1][2] + positions[i-1][4])/2,(positions[i-1][3] + positions[i-1][5])/2)
        pt2 = ((positions[i][2] + positions[i][4])/2,(positions[i][3] + positions[i][5])/2)

        lines.append([positions[i][0],pt1,pt2])
    
    frame_num = 0
    while True: # while video is running
        return_value, frame = vid.read()
        if not return_value:
            print('Video has ended or failed!')
            break
        frame_num +=1
        for line in lines:
            if line[0] <= frame_num:
                cv.line(frame,line[1],line[2],(0,255,0),2)
        out.write(frame)


        



# calculate centers of bounding boxes
def get_centers(id,results):
    centers = []
    for box in results[id]:
        centers.append([box[0],(box[2] + box[4])/2,(box[3] + box[5])/2])
    return centers


