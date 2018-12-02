# Kevin is a freelance video producer who makes TV commercials for local
# businesses. When he makes a commercial, he usually films several short
# videos. Later, he puts these short videos together to make the final
# commercial. He has asked you to write the following two programs.

#   1. A program that allows him to enter the running time (in seconds)
#   of each short video in a project. The running times are saved to a file.

#   2. A program that reads the contents of the file, displays the running
#   times, and then displays the total running time of all the segments.


# Here is the general algorithm for the first program, in pseudocode:
#   Get the number of videos in the project.
#   Open an output file.
#   For each video in the project:
#       Get the video's running time.
#       Write the running time to the file.
#   Close the file.

# This program saves a sequence of video running times to the 
# video_times.txt file.

def write():
    # Get the number of videos in the project.
    print()
    num_videos = int( input('How many videos are in the project? '))

    # open the file to hold the running times.
    video_file = open('video_times.txt', 'w')

    # Get each video running time and write it to the file
    print()
    print('Enter the running times for each video.')
    for count in range(1, num_videos + 1):
        run_time = float( input('Video #' + str(count) + ': '))
        video_file.write( str(run_time) + '\n')
    # Close the file
    video_file.close()
    print('The times have been saved to video_times.txt')
    print()

# Here is the general algorithm for the second program:
#   Initialize an accumulator to 0.
#   Initialize a count variable to 0.
#   Open the input file.
#   For each line in the file:
#       - Convert the line to a floating-point number. (This is the running
#       time for a video.)
#       - Add one to the count variable. (This keeps count of the number
#       of videos.)
#       - Display the running time for this video.
#       - Add the running time to the accumulator.
#   Close the file.
# Display the contents of the accumulator as the total running time

def read():
    # Open the video_times.txt file for reading
    video_file = open('video_times.txt', 'r')

    # Initialize an accumulator to 0.0
    total = 0.0

    # Initialize a variable to keep count of the videos
    count = 0

    print()
    print('Here are the running times for each video: ')
    
    # Get the value from tje file and total them
    for line in video_file:
        run_time = float(line) # Convert a line to a float
      
        # Add 1 to the count variable.
        count += 1
      
        # Display the time
        print('Video #', count, ': ', run_time, sep='')
      
        # Add the time to total
        total += run_time
    # Close the file
    video_file.close()

    # Display the total of the running times.
    print('The total running time is', total, 'seconds.')
    print()

def main():
    write()
    read()

# Call the main function
main()

