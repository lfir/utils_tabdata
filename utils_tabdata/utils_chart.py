import matplotlib.pyplot as plt


class UtilsChart:
    @staticmethod
    def plot_timecomplexity(inputsizes, datadict, title=""):
        """Creates and displays a line chart with input size values on the X-axis
        and execution time values on the Y-axis.

        Positional arguments:
        inputsizes -- Contains the X-axis labels (index in Pandas).
        datadict -- The Y-axis values. Each key represents a column and has
        a list of execution times as value. More details about this data format can be found at:
        https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#from-dict-of-series-or-dicts
        title -- Optional. The title of the chart.

        Example:
        plot_timecomplexity(
            [1000, 2000, 3000],
            {'merge_sort': [50, 500, 5000], 'bubble_sort': [150, 600, 8000]}
        )
        """
        plt.title(title)
        plt.xticks(range(len(inputsizes)), inputsizes)
        plt.xlabel("Input size")
        plt.ylabel("Execution time")
        plt.grid(True, color="gray", linestyle="solid")

        for t in datadict.items():
            plt.plot(t[1], label=t[0])

        plt.legend().set_visible(True)

        plt.show()
