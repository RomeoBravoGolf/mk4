import face_recognition
import cv2
import numpy as np

def analyze(video):
    video_capture = cv2.VideoCapture(video)

     #buscar framerate
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print('el video tiene ', fps, ' efepeeses')

    macri = face_recognition.load_image_file("macri.jpg")
    macri_encoding = face_recognition.face_encodings(macri)[0]

    bergman = face_recognition.load_image_file("bergman.jpg")
    bergman_encoding = face_recognition.face_encodings(bergman)[0]

    larreta = face_recognition.load_image_file("larreta.jpg")
    larreta_encoding = face_recognition.face_encodings(larreta)[0]

    malcorra = face_recognition.load_image_file("malcorra.jpg")
    malcorra_encoding = face_recognition.face_encodings(malcorra)[0]

    frigerio = face_recognition.load_image_file("frigerio.jpg")
    frigerio_encoding = face_recognition.face_encodings(frigerio)[0]

    pinedo = face_recognition.load_image_file("pinedo.jpg")
    pinedo_encoding = face_recognition.face_encodings(pinedo)[0]

    lombardi = face_recognition.load_image_file("lombardi.jpg")
    lombardi_encoding = face_recognition.face_encodings(lombardi)[0]


    known_face_encodings = [
        macri_encoding, bergman_encoding, larreta_encoding, malcorra_encoding, frigerio_encoding, pinedo_encoding, lombardi_encoding
    ]
    known_face_names = [
        "Mauricio Macri", "ingmar Bergman", "Horacio Larreta", "Susana Malcorra", "Rogelio Frigerio", "Federico Pinedo", "Hernan Lombardi"
    ]
    counter = [0, 0, 0, 0, 0, 0, 0]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        #crear .csv
        csv = open("log.csv", "w+")
        csv.write("name, total time\n")
        for zz in range(7):
            body = known_face_names[zz], counter[zz]
            body = str(body).replace(")", "\n").replace("'","").replace("(","")
            csv.write(body)
        csv.close()
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

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
                            counter[xx] += 1/fps
                for yy in range(7):
                    print(known_face_names[yy], counter[yy])


                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video_capture.release()
    cv2.destroyAllWindows()