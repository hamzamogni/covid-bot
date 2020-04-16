<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Message extends Model
{
    protected $fillable = ["message"];


    public function replies()
    {
    	return $this->hasMany("App\Message", "parent_id");
    }

    public function parent()
    {
    	return $this->belongsTo("App\Message");
    }

    public function is_reply()
    {
    	return $this->parent_id != null;
    }


}
