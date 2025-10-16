def calculate_average_review_rating(reviews):
    if not reviews:
        return None
        try:
            total_rating  = sum(review['rating'] for review in reviews)
            average_rating = total_rating / len(reviews)
            return float(average_rating)
        except(KeyError, TypeError) as e:
            print(f"Error calculating average rating: {e}")
            return None
         if __name__ == "__main__":
            sample_reviews = [
                {'rating': 4},
                {'rating': 5},
                {'rating': 6}
            ]                                          
            average_rating = calculate_average_review_rating(sample_reviews)
            print(f"Average ratng:{average_rating}")
            empty_reviews = []
            average_rating_empty = calculate_average_review_rating(empty_reviews)
            print(f"Average rating (empty): {average_rating_empty}")