import obd

# help(obd.commands)

# speed_cmd = obd.commands.SPEED
# rpm_cmd = obd.commands.RPM
# throttle_cmd = obd.commands.THROTTLE_POS

connection = obd.OBD()

bad_keys = ['modes', 'OBD_COMPLIANCE', 'ELM_VERSION', 'ELM_VOLTAGE']
cmds = {key: cmd for key, cmd in obd.commands.__dict__.items() if key not in bad_keys and 'O2' in key} # and connection.supports(cmd)}
print(cmds)


if connection.is_connected():

    print('start')
    file = open('obd_test.txt', 'w')
    file.write(','.join([key for key in cmds.keys()]) + '\n')
    for i in range(10):
        results = []
        for key, cmd in cmds.items():
            print(key)
            val = str(connection.query(cmd).value).split()[0]
            results.append(val)
        file.write(','.join([r for r in results]) + '\n')
    file.close()

    print('end')


# cap = cv2.VideoCapture(0)

# while True:
#   ret, frame = cap.read()
#   cv2.imshow('frame', frame)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#       break

# cap.release()
# cv2.destroyAllWindowss
