def solution(genres, plays):
    answer = []
    
    genre_total_play = {} 
    genre_songs = {}      
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        genre_total_play[genre] = genre_total_play.get(genre, 0) + play
        
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, i))

    sorted_genres = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        answer.extend([song[1] for song in songs[:2]])
        
    return answer