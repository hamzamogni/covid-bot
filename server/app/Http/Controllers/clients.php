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
    	$message = $request->message;
        
        $response = Http::post("http://localhost:5000/", [
            "message" => $message
        ]);



    	return Response($response);
    }
}
