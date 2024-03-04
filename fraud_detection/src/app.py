import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, utils_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

import grpc
from concurrent import futures

# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.HelloServiceServicer
class fraud_detection(fraud_detection_grpc.fraud_detectionServicer):
    # Create an RPC function to say hello
    def fraud_detection(self, request, context):
        # Create a HelloResponse object
        response = fraud_detection.f_detectionResponse()
        possible_fraud_ids = [123, 456, 789]
        if request.name and request.id:
            for combination in possible_fraud_ids:
                if combination in request.id :
                    response.is_fraud = True
                else:
                    response.is_fraud = False
        else:
            response.is_fraud = True
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    fraud_detection_grpc.add_fraud_detectionServicer_to_server(fraud_detection(), server)
    # Listen on port 50051
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50051.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()