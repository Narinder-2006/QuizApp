# QuizApp - Python Quiz Application



This Python-based quiz application allows users to take a quiz on various programming topics such as Lists, Strings, Dictionaries, Operators, and Functions. The quiz is divided into three difficulty levels: Easy, Medium, and Hard. Users are presented with questions randomly selected from these categories, and their performance is tracked in terms of both accuracy and time taken for each question.

## Features

- **Dynamic Question Selection**: Select questions from multiple topics like Lists, Strings, Dictionaries, Operators, and Functions.
- **Difficulty Levels**: Choose between Easy, Medium, or Hard questions for each topic.
- **Time Tracking**: Measures the time taken for each question.
- **Accuracy Calculation**: Shows the percentage of correct answers for each topic.
- **Results Visualization**: Displays the results in a graphical format (Accuracy by Topic and Time Taken per Question) using matplotlib.

## Installation

To run this quiz application, you need Python 3.x installed on your system along with the required dependencies. Follow these steps to set up the project:

1. Clone the repository:

    ```bash
    https://github.com/Narinder-2006/QuizApp.git
    cd QuizApp
    ```

2. Install the required Python libraries:

    ```bash
    pip install matplotlib
    ```



## File Structure

The project should follow this structure:
/QuizApp /questions /Lists Easy.txt Medium.txt Hard.txt /Strings Easy.txt Medium.txt Hard.txt /Dictionaries Easy.txt Medium.txt Hard.txt /Operators Easy.txt Medium.txt Hard.txt /Functions Easy.txt Medium.txt Hard.txt /answers /Lists Easy.txt Medium.txt Hard.txt /Strings Easy.txt Medium.txt Hard.txt /Dictionaries Easy.txt Medium.txt Hard.txt /Operators Easy.txt Medium.txt Hard.txt /Functions Easy.txt Medium.txt Hard.txt quiz.py README.md requirements.txt

## Usage

1. Run the quiz script:

    ```bash
    main.py
    ```

2. You will be prompted to choose a difficulty level (Easy, Medium, or Hard) and the number of questions for each topic.
3. The quiz will display questions one by one. Type your answer and press Enter.
4. After completing the quiz, your accuracy and time taken for each question will be displayed, and the results will be visualized in two bar charts:
   - **Accuracy by Topic**: The percentage of correct answers per topic.
   - **Time Taken per Question**: The time taken for each question in seconds.

## Example Flow

Enter Difficulty mode of Quiz (Easy, Medium and Hard): Easy Enter the number of topics: Lists Dictionaries Strings Operators Functions

![example](./images\starting.JPG)

## Results Visualization

Here’s an example of what the results look like:

### Accuracy by Topic

This chart displays the accuracy percentage for each topic in the quiz. A higher percentage means better performance!



### Time Taken per Question

This chart displays the time taken for each question, measured in seconds. A lower value indicates quicker responses!

![Time Taken and Accuracy per Question](./images\graphs.JPG)

### Full Results Example

Here’s a complete visual summary of your quiz performance:

![Full Results Example](./images\quespreview.JPG)

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. You can also open issues to report bugs or suggest improvements.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new pull request



## Acknowledgments

- [matplotlib](https://matplotlib.org/) for the charting library
- Open-source contributors and communities that help in learning and development



