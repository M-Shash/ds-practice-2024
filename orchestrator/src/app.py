import sys
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import grpc
# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
fraud_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, fraud_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc
recommendation_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/recommendation'))
sys.path.insert(0, recommendation_path)
import recommendation_pb2 as recommendation
import recommendation_pb2_grpc as recommendation_grpc
t_verification_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, t_verification_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc


# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app)



def detect_fraud(name , id ):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.fraud_detectionStub(channel)
        # Call the service through the stub object.
        request = fraud_detection.f_detectionRequest(name=name, id=id)
        response = stub.fraud_detect(request)
    return response.is_fraud


# Function to handle checkout processing
def process_checkout(request_data):
    # Dummy logic 
    # Call fraud detection gRPC service
    fraud_response = detect_fraud(name='orchestrator')
    order_status_response = {
        'orderId': '12345',
        'status': 'Order Approved',
        'suggestedBooks': [
            {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
            {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
        ]
    }
    return order_status_response


@app.route('/', methods=['GET'])
def index():
    """
    Responds with 'Hello, [name]' when a GET request is made to '/' endpoint.
    """
    # Test the fraud-detection gRPC service.
    response = greet(name='orchestrator')
    # Return the response.
    return response

@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        # Get data from request
        request_data = request.json

        # Create worker thread for processing checkout
        checkout_thread = threading.Thread(target=process_checkout, args=(request_data,))
        checkout_thread.start()

        # Return immediate response to the client
        return jsonify({'message': 'Checkout processing started in parallel.'}), 202

    except Exception as e:
        # Handle exceptions and return appropriate error response
        error_response = {'error': {'code': '500', 'message': str(e)}}
        return jsonify(error_response), 500


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
