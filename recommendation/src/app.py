import grpc
from concurrent import futures
import recommendation_pb2 as recommendation
import recommendation_pb2_grpc as recommendation_grpc

class RecommendationService(recommendation_grpc.RecommendationServiceServicer):
    def GetRecommendations(self, request, context):
        # Static list of recommended items
        recommendations = [
            recommendation.RecommendationItem(itemId='1', itemName='Item 1'),
            recommendation.RecommendationItem(itemId='2', itemName='Item 2'),
            recommendation.RecommendationItem(itemId='3', itemName='Item 3'),
            # Add more items as needed
        ]
        # Create and return the response
        return recommendation.RecommendationResponse(recommendations=recommendations)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    recommendation_grpc.add_RecommendationServiceServicer_to_server(RecommendationService(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("Server started. Listening on port 50053.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
