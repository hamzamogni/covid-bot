<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

use Illuminate\Support\Facades\Http;

class clients extends Controller
{
    public function predict(Request $request)
    {
    	$validator = $request->validate([
	        'message' => 'required|min:1',
	    ]);
	    
    	$message = $request->message;

    	if(env("BOT_MAINTENANCE") == true){
    		$response = [
    			"status" => "maintenance",
    			"message" => "انا سهم، وانا تحت الصيانة دابا والفريق اللي قادني كايعطيني معلومات أكثر باش نعرف نجاوب حسن على الاسئلة ديالكم"
    		];
    		return Response($response);
    	}

        $response = Http::post("http://localhost:5000/", [
            "message" => $message
        ]);

    	return Response($response);
    }
}
