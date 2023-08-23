import csv
import cv2
# import HandTrackingModule as htm
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time

width = 1280
height = 720
cap = cv2.VideoCapture(1)
cap.set(3,width)
cap.set(4,height)
cap.set(10,250)

detector = HandDetector(detectionCon=0.8)
class MCQ:
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])

        self.userAns = None

    def update(self, cursor, bboxes):

        for x,bbox in enumerate(bboxes):
            x1,y1,x2,y2 = bbox
            if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                self.userAns = x+1
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), cv2.FILLED)





# Import csv file data
pathCSV = "Quiz.csv"
with open(pathCSV, newline="\n") as f:
    reader = csv.reader(f)
    dataALL = list(reader)[1:]
# print(len(dataALL))

# Create object for each question
mcqList = []
for q in dataALL:
    mcqList.append(MCQ(q))

print(len(mcqList))

qNo = 0
qTotal = len(dataALL)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if qNo < qTotal:
        mcq = mcqList[qNo]

        img, bbox = cvzone.putTextRect(img, mcq.question, [100,100], 1.75, 2, offset=40, border=3)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [100,250], 1.75, 2, offset=40, border=3)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [500,250], 1.75, 2, offset=40, border=3)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [100,400], 1.75, 2, offset=40, border=3)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [500,400], 1.75, 2, offset=40, border=3)

        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]
            length, info, img = detector.findDistance(lmList[4], lmList[8], img)
            # print(length)
            if length<30:
                mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])
                print(mcq.userAns)
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    qNo += 1
    else:
        score = 0
        for mcq in mcqList:
            if mcq.answer == mcq.userAns:
                score += 1
        score = round((score/qTotal)*100,2)
        img, _ = cvzone.putTextRect(img, "Quiz Completed", [250, 300], 1.75, 2, offset=50, border=5)
        img, _ = cvzone.putTextRect(img, f'Your Score: {score}%', [700, 300], 1.75, 2, offset=50, border=5)

        # print(score)

    # Draw Progress Bar
    barValue = 150 + (950//qTotal)*qNo
    cv2.rectangle(img, (150,600), (barValue, 650), (0,155,0), cv2.FILLED)
    cv2.rectangle(img, (150,600), (1100, 650), (17, 0, 153), 5)
    img, _ = cvzone.putTextRect(img, f'{round((qNo/qTotal)*100)}%', [1130, 635], 1.75, 2, offset=16)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break