import argparse
import udpserver as udps
import udpclient as udpc

des="smdh --a simple messaging and data handling tool"

parser = argpars.ArgumentParser(
        description=des,
        epilog="shaking my damn head"
        )

parser.add_argument(
        'port', metavar='-p',
        type=int,
        help='define a port'
        )

parser.add_argument(
        'buff',
        metavar='-b',
        type=int, 
        help='define a buffer'
        )         

parser.add_argument(
        'verbosity',
        metavar='-v',
        type=lambda verbosity: Verbosity[verbosity],
        choices=list(Verbosity)
        )

parser.add_arguemtn(
        'message'
        metavar='-m',
        help='the message you wish to send'
        )

args = parser.parse_args()




