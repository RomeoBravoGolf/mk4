import face_recognition
import cv2
import numpy as np
from datetime import datetime
import os

def analyze(video):
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("el video empezo a las ", start_time)
    video_capture = cv2.VideoCapture(video)

    # buscar framerate
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    known_face_names = []
    known_face_encodings = []
    counter = []

    for filename in os.listdir("../resources/"):
        known_face_names.append(filename[:-4])
        counter.append(0)
        encoding = face_recognition.load_image_file("../resources/"+filename)
        known_face_encodings.append(face_recognition.face_encodings(encoding)[0])

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        try:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        except Exception as e:
            break

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    for xx in range(7):
                        if name == known_face_names[xx]:
                            counter[xx] += 1 / fps
                #for yy in range(7):
                #    print(known_face_names[yy], counter[yy])

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        # for (top, right, bottom, left), name in zip(face_locations, face_names):
        #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4
        #
        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #
        #     # Draw a label with a name below the face
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        #
        # # Display the resulting image
        # cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    filename = video[:-3] + ".csv"

    csv = open(filename, "w+")

    write = str("name, total time\n")
    csv.write(write)

    for zz in range(7):
        appearence_time = counter[zz] if counter[zz] > 1 else 0
        body = known_face_names[zz], appearence_time
        body = str(body).replace(")", "\n").replace("'", "").replace("(", "")
        csv.write(body)
    csv.close()

    video_capture.release()
    cv2.destroyAllWindows()

    os.system("rm "+video)