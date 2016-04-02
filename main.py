import numpy as np
import matplotlib.pyplot as plt
import merwmidi as mm
import merw as mw

if __name__ == '__main__':
    """ what up """
    # How many steps will walker walk
    nof_steps = 2500

    # TODO New interface:
    # hands = create_hands()
    # for _ in range(nof_steps):
    #     for finger in hands:
    #         finger.play(c_time)
    #         c_time += dt
    # notes = hands.get_notes()
    # create_midi(notes)

    # How many positions can walker occupy
    nof_spots = 80

    # Handles probabilities and potentials
    # TODO Some grander container for multiple 
    # walkers is desired, preferably some 
    # Merw with walkers in rhythm?
    walker = mw.Walker(nof_spots)
    e_walker = mw.Walker(nof_spots)

    # Does research
    histogram = np.zeros(nof_spots)
    e_histogram = np.zeros(nof_spots)

    # Pitches are what we actually calculate
    # and they start from 30 and iterate like indexes
    pitches = [x + 30 for x in range(nof_spots)]

    # Merw starting position set
    pos = 33
    e_pos = 66
    positions = []
    e_positions = []

    # First orbit 50
    walker.set_prefered(50)
    walker.set_scale_shift(0)

    # Shift C -> E
    e_walker.set_prefered(50)
    e_walker.set_scale_shift(4)

    for it in range(nof_steps):
        # Histogram
        histogram[pos] += 1
        e_histogram[e_pos] += 1

        positions.append(pos)
        e_positions.append(e_pos)
        next_pos = walker.get_next_value(pos)
        e_next_pos = e_walker.get_next_value(e_pos)

        # pyDebug() <<
        if it%2000 == 0:
            debug = "Iteration: {}\nPosition: {}"
            print debug.format(it, pos)

        # Move, actually
        pos = next_pos
        e_pos = e_next_pos

    # TODO rediscover this
    # Create final pitches vector
    # walker_pitches = [pitches[pos] for pos in positions]
    # Make midi file with calculated pitches
    # mm.make_midi(walker_pitches)

    plt.bar(pitches, histogram, color = 'r', alpha = 0.5)
    plt.bar(pitches, e_histogram, color = 'c', alpha = 0.5)
    plt.show()

    plt.plot(positions, 'ko', alpha = 0.7)
    plt.plot(positions, 'k--', alpha = 0.4)
    plt.plot(e_positions, 'co', alpha = 0.7)
    plt.plot(e_positions, 'c--', alpha = 0.4)
    plt.show()
