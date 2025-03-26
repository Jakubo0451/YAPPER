from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from models import TweetsModel
from schemas import TweetCreate, TweetResponse

router = APIRouter(
    prefix="/tweets",
    tags=["tweets"]
)

# endpoints for tweets, get all tweets, create tweet, edit tweet and delete tweet 
@router.get("", response_model=List[TweetResponse])
def read_tweets(db: Session = Depends(get_db)):
    tweets = db.query(TweetsModel).all()
    return tweets

@router.post("", response_model=TweetResponse)
def create_tweet(tweet: TweetCreate, db: Session = Depends(get_db)):
    tweet = TweetsModel(tweet=tweet.tweet, user_id=tweet.user_id, tags=tweet.tags)
    db.add(tweet)
    db.commit()
    db.refresh(tweet)
    return tweet

@router.put("/{tweet_id}")
def update_tweet(tweet_id: int, tweet: TweetCreate, db: Session = Depends(get_db)):
    tweet = db.query(TweetsModel).filter(TweetsModel.id == tweet_id).first()
    tweet.tweet = tweet.tweet
    tweet.user_id = tweet.user_id
    tweet.tags = tweet.tags
    db.commit()
    return {"message": "Tweet updated successfully"}

@router.delete("/{tweet_id}")
def delete_tweet(tweet_id: int, db: Session = Depends(get_db)):
    tweet = db.query(TweetsModel).filter(TweetsModel.id == tweet_id).first()
    db.delete(tweet)
    db.commit()
    return {"message": "Tweet deleted successfully"}