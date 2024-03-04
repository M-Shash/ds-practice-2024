import grpc
from concurrent import futures
import re
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

class TransactionVerificationService(transaction_verification_grpc.TransactionVerificationServiceServicer):
    def VerifyTransaction(self, request, context):
        # Perform sanity checks on the input data
        if not self._is_valid_credit_card(request.creditCardNumber):
            return transaction_verification.TransactionVerificationResponse(isValid=False, errorMessage="Invalid credit card format")
        if not self._is_required_fields_filled(request):
            return transaction_verification.TransactionVerificationResponse(isValid=False, errorMessage="Missing required fields")
        
        # Any Other ideas...
        return transaction_verification.TransactionVerificationResponse(isValid=True, errorMessage=None)

    def _is_valid_credit_card(self, credit_card_number):
        # Simple regex pattern for credit card format validation
        pattern = r'^\d{16}$'
        return re.match(pattern, credit_card_number)

    def _is_required_fields_filled(self, request):
        required_fields = [
            request.userName,
            request.userContact,
            request.creditCardNumber,
            request.creditCardExpirationDate,
            request.creditCardCVV
        ]
        return all(required_fields)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    transaction_verification_grpc.add_TransactionVerificationServiceServicer_to_server(TransactionVerificationService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Server started. Listening on port 50052.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
