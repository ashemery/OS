#!/usr/bin/python

from threading import Thread
from processing import Process

class threads_object(Thread):
    def run(self):
        function_to_run()

class nothreads_object(object):
    def run(self):
        function_to_run()

class process_object(Process):
    def run(self):
        function_to_run()

def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()

def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

def processed(num_processes):
    funcs = []
    for i in range(int(num_processes)):
        funcs.append(process_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

def show_results(func_name, results):
    print "%-23s %4.6f seconds" % (func_name, results)

if __name__ == "__main__":
    import sys
    from timeit import Timer

    repeat = 100
    number = 1

    num_threads = [ 1, 2, 4, 8 ]

    if len(sys.argv) < 2:
        print 'Usage: %s module_name' % sys.argv[0]
        print '  where module_name contains a function_to_run function'
        sys.exit(1)
    module_name = sys.argv[1]
    if module_name.endswith('.py'):
        module_name = module_name[:-3]
    print 'Importing %s' % module_name
    m = __import__(module_name)
    function_to_run = m.function_to_run

    print 'Starting tests'
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non_threaded (%s iters)" % i, best_result)

        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)

        t = Timer("processed(%s)" % i, "from __main__ import processed")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("processes (%s procs)" % i, best_result)
        print "\n",

    print 'Iterations complete'