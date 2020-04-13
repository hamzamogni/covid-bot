<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class clients extends Controller
{
    public function predict(Request $request)
    {
    	$message = $request->message;
    	// $cmd = escapeshellcmd("python3 " . env("MODEL_CLIENT_PATH") . " \"" . $message . " \"");

    	$process = new Process(["python3", env("MODEL_CLIENT_PATH"), $message]);
		$process->run();

		// executes after the command finishes
		if (!$process->isSuccessful()) {
		    throw new ProcessFailedException($process);
		}

		$output = $process->getOutput();



    	return Response($output);
    }
}
