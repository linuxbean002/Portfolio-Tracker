#------------Necessary Variables--------------#
import datetime as dt
symbols = ['AAPL', 'MMM', 'INTC', 'JPM', 'DE', 'WFC', 'BK', 'PM', 'HD', 'GE']
allocations = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
start_date = dt.date(2017,01,03)

#Benchmark Index
bench_symbol = "SPY"

#RF Syntax: 6 MO, 2 YR etc.
rate = '1 YR'
#CUR, AVG
method = "AVG"

#For Quandl
api_key = ""

#Dirctory Input For Data and Reports
root_path = "C:/Users/fdupu/PycharmProjects/Portfolio Tracker"

#------------Run Program----------------------#
if __name__ == '__main__':
    import rebalance
    rebalance.rebalance(allocations=allocations)
    # # 1.) Import the module
    # import report
    #
    # # Select Functions
    #end_date = dt.date.today()

    # r = report.rep(fname=root_path + '/Reports/Daily Report ' + str(end_date) + '.pdf',fund_name="Valhalla Investments LLC",logo_path="C:/Users/fdupu/Desktop/logo.png")
    # r.cover()
    # r.perf()
    # r.mets()
    # r.diversification()
    # r.savePDF()