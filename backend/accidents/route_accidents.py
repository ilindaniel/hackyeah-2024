import json
import translate_file_to_eng

accident_file_base = "bf_ids.json"
accident_file = "bf_ids_eng.json"

def coords_match(crash_point, point1, point2, accuracy=0.00001):
    extrema_x = {}
    extrema_y = {}
    extrema_x[0] = min(point1[0], point2[0])
    extrema_x[1] = max(point1[0], point2[0])
    extrema_y[0] = min(point1[1], point2[1])
    extrema_y[1] = max(point1[1], point2[1])
    if extrema_y[0] - accuracy > crash_point[1] or extrema_y[1] + accuracy < crash_point[1]:
        return False

    if extrema_x[0] - accuracy > crash_point[0] or extrema_x[1] + accuracy < crash_point[1]:
        return False

    return True


def get_route_accidents(route):
    global accident_file, accident_file_base

    translate_file_to_eng.translate_file(accident_file_base, accident_file)
    accidents = {}

    with open(accident_file, 'r') as f:
        data = json.load(f)
        for key_crashes, value_crashes in data.items():
            crash_vals = {}
            crash_vals[0] = value_crashes['gps_y']
            crash_vals[1] = value_crashes['gps_x']
            for i in range(len(route) - 1):
                point1 = route[i]
                point2 = route[i + 1]
                #print(point1)
                #print(point2)
                if coords_match(crash_vals, point1, point2):
                    print(f"match: crash: {crash_vals}; p1: {point1}; p2: {point2}")
                    accidents[key_crashes] = value_crashes
    return accidents

def score_accident(route):
    multiplier = 1.0
    accidents = get_route_accidents(route)
    for _, accident in accidents.items():  # Unpack key-value pair, but we don't need the key
        for participant in accident['participants'].values():  # Access each participant
            for victim_type, victim_data in participant['victims'].items():  # Access the victims
                for injury in victim_data['injuries']:  # Iterate through the injuries list
                    if injury == 'No injuries':
                        multiplier += 0.3
                    elif injury == 'Minor':
                        multiplier += 1
                    elif injury == 'Severe':
                        multiplier += 4
                    elif injury == 'Dead on spot of accident':
                        multiplier += 7
    return multiplier










if __name__ == '__main__':
    dummy_route = [
	[
		50.0634159,
		19.9329681
	],
	[
		50.0632718,
		19.9328029
	],
	[
		50.0626276,
		19.9320892
	],
	[
		50.0620745,
		19.9335343
	],
	[
		50.062038,
		19.933625
	],
	[
		50.0617709,
		19.9342894
	],
	[
		50.062523,
		19.9349872
	],
	[
		50.0632688,
		19.9357144
	],
	[
		50.0633444,
		19.9355881
	],
	[
		50.0639207,
		19.936112
	],
	[
		50.0639732,
		19.9361602
	],
	[
		50.0642714,
		19.9351947
	],
	[
		50.0647684,
		19.9366835
	],
	[
		50.0648199,
		19.9368303
	],
	[
		50.0648458,
		19.936904
	],
	[
		50.0653868,
		19.9371071
	],
	[
		50.0653243,
		19.9387072
	],
	[
		50.0647665,
		19.9397421
	],
	[
		50.0642,
		19.9393552
	],
	[
		50.063982,
		19.9391896
	],
	[
		50.063656,
		19.938951
	],
	[
		50.0631804,
		19.9386136
	],
	[
		50.0631412,
		19.9385853
	],
	[
		50.0624762,
		19.9410176
	],
	[
		50.0616829,
		19.940424
	],
	[
		50.0612771,
		19.9418132
	],
	[
		50.0613505,
		19.9432247
	],
	[
		50.0611665,
		19.9441134
	],
	[
		50.062778,
		19.9449678
	],
	[
		50.0633876,
		19.9450642
	]
]
    result = get_route_accidents(dummy_route)
    score = score_accident(dummy_route)
    #print(f"result 1:{result}")
    print(f"result 1 score:{score}")

    dummy_route2 = [
	[
		50.0632718,
		19.9328029
	],
	[
		51.1181104,
		20.2761937
	],
	[
		50.0626276,
		19.9320892
	],
	[
		50.0620745,
		19.9335343
	],
	[
		50.062038,
		19.933625
	],
	[
		50.0617709,
		19.9342894
	],
	[
		50.062523,
		19.9349872
	],
	[
		50.0632688,
		19.9357144
	],
	[
		50.0633444,
		19.9355881
	],
	[
		50.0639207,
		19.936112
	],
	[
		50.0639732,
		19.9361602
	],
	[
		50.0642714,
		19.9351947
	],
	[
		50.0647684,
		19.9366835
	],
	[
		50.0648199,
		19.9368303
	],
	[
		50.0648458,
		19.936904
	],
	[
		50.0653868,
		19.9371071
	],
	[
		50.0653243,
		19.9387072
	],
	[
		50.0647665,
		19.9397421
	],
	[
		50.0642,
		19.9393552
	],
	[
		50.063982,
		19.9391896
	],
	[
		50.063656,
		19.938951
	],
	[
		50.0631804,
		19.9386136
	],
	[
		50.0631412,
		19.9385853
	],
	[
		50.0624762,
		19.9410176
	],
	[
		50.0616829,
		19.940424
	],
	[
		50.0612771,
		19.9418132
	],
	[
		50.0613505,
		19.9432247
	],
	[
		50.0611665,
		19.9441134
	],
	[
		50.062778,
		19.9449678
	],
	[
		50.0633876,
		19.9450642
	]
]
    result2 = get_route_accidents(dummy_route2)
    score2 = score_accident(dummy_route2)
    #print(f"result 2:{result2}")
    print(f"result 2 score:{score2}")
