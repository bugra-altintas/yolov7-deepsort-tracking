import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

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

def draw_tracking_lines(results,videopath,output_path,bee_id=None):
    # read video
    vid = cv.VideoCapture(videopath)
    width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))  # by default VideoCapture returns float instead of int
    height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = int(vid.get(cv.CAP_PROP_FPS))
    codec = cv.VideoWriter_fourcc(*"XVID")
    out = cv.VideoWriter(output_path, codec, fps, (width, height))

    if bee_id is None:
        allLines = {}
        for bid in results:
            pos = results[bid]
            lines = []
            for i in range(1,len(pos)-1):
                pt1 = (int((pos[i-1][2] + pos[i-1][4])/2),int((pos[i-1][3] + pos[i-1][5])/2))
                pt2 = (int((pos[i][2] + pos[i][4])/2),int((pos[i][3] + pos[i][5])/2))
                lines.append([pos[i][0],pt1,pt2])
            allLines[bid] = lines
        frame_num = 0
        while True: # while video is running
            return_value, frame = vid.read()
            if not return_value:
                print('Video has ended or failed!')
                break
            frame_num +=1
            print("Frame",frame_num)
            cmap = plt.get_cmap('tab20b') #initialize color map
            colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]
            for bid in allLines:
                lines = allLines[bid]
                color = colors[int(bid) % len(colors)]
                color = [i * 255 for i in color]
                for line in lines:
                    if line[0] <= frame_num:
                        cv.line(frame,line[1],line[2],color,2)
            out.write(frame)
    elif len(bee_id) > 1:
        allLines = {}
        for bid in bee_id:
            pos = results[bid]
            lines = []
            for i in range(1,len(pos)-1):
                pt1 = (int((pos[i-1][2] + pos[i-1][4])/2),int((pos[i-1][3] + pos[i-1][5])/2))
                pt2 = (int((pos[i][2] + pos[i][4])/2),int((pos[i][3] + pos[i][5])/2))
                lines.append([pos[i][0],pt1,pt2])
            allLines[bid] = lines
        frame_num = 0
        while True: # while video is running
            return_value, frame = vid.read()
            if not return_value:
                print('Video has ended or failed!')
                break
            frame_num +=1
            print("Frame",frame_num)
            cmap = plt.get_cmap('tab20b') #initialize color map
            colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]
            for bid in allLines:
                lines = allLines[bid]
                color = colors[int(bid) % len(colors)]
                color = [i * 255 for i in color]
                for line in lines:
                    if line[0] <= frame_num:
                        cv.line(frame,line[1],line[2],color,2)
            out.write(frame)

    else:
        positions = results[bee_id[0]]
        lines = []

        for i in range(1,len(positions)-1):
            pt1 = (int((positions[i-1][2] + positions[i-1][4])/2),int((positions[i-1][3] + positions[i-1][5])/2))
            pt2 = (int((positions[i][2] + positions[i][4])/2),int((positions[i][3] + positions[i][5])/2))

            lines.append([positions[i][0],pt1,pt2])
    
        frame_num = 0
        while True: # while video is running
            return_value, frame = vid.read()
            if not return_value:
                print('Video has ended or failed!')
                break
            frame_num +=1
            print("Frame",frame_num)
            cmap = plt.get_cmap('tab20b') #initialize color map
            colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]
            
            color = colors[bee_id[0] % len(colors)]  # draw bbox on screen
            color = [i * 255 for i in color]

            for line in lines:
                if line[0] <= frame_num:
                    cv.line(frame,line[1],line[2],color,2)
            
            out.write(frame)
    out.release()
# calculate centers of bounding boxes
def get_centers(id,results):
    centers = []
    for box in results[id]:
        centers.append([box[0],(box[2] + box[4])/2,(box[3] + box[5])/2])
    return centers


