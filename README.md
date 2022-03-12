# RIS2CSV

RIS2CSV Convert RIS files from [Scopus](https://www.scopus.com/) to CSV files for easier data analysis.  
Output CSV file uses tab **'\t'** as delimiter.  

It was created because there are problems with downloading CSV files from
the [Scopus](https://www.scopus.com/) platform and other formats being more difficult to create analyzes with Excel.  

You can also use it to convert RIS file to Python Dictionary to do data analysis with Python.

- ## How to install and run

- ### Cloning the repository
  To clone the repository run the following command:
  ```
  $ git clone https://github.com/WeDias/RIS2CSV.git
  ```

- ### Running CLI application
    Inside the **/src** folder run the command below:
    ```
    $ python main.py -i <inputfile> -o <outputfile>
    ```
    Example:
    ```
    $ python main.py -i ../resources/example.ris -o ../resources/output_example.csv
    ```

- ### Running GUI application
    Inside the **/src** folder run the command below:
    ```
    $ python execute.pyw
    ```
    Or just double click on the file execute.pyw
