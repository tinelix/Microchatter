package ru.tinelix.microbot.core;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.nio.file.*;

import com.ea.async.Async;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;
import com.fasterxml.jackson.databind.ObjectMapper;

import ru.tinelix.microbot.core.interfaces.LogColorFormatter;

public class Microbot extends TelegramLongPollingBot implements LogColorFormatter {
		
	public class MicrobotConfig {
		public String 	tg_token;
		public String 	tg_username;
		public String 	name;
		public long   	tg_bot_owner_id;
		public boolean	use_irc_bridge;
		public String 	irc_server;
		public int	  	irc_port;
		public String 	irc_encoding;
		public String 	irc_nickname;
		public String 	irc_ns_passwd;
		public String 	license;
	}	
		
	private MicrobotConfig config;
	private static String VERSION = "0.0.0";
		
	public static final String RESET_COLOR 		= "\u001B[0m";
	public static final String SUCCESS_COLOR 	= "\u001B[32m"; // Green
	public static final String WARNING_COLOR 	= "\u001B[33m"; // Yellow
	public static final String ERROR_COLOR 		= "\u001B[31m"; // Red
	public static final String INFO_COLOR      	= "\u001B[36m"; // Cyan
		
	public Microbot() {
			this.config = new MicrobotConfig();
			try {
				FileInputStream inputStream = new FileInputStream("config/bot.json");
				ObjectMapper mapper = new ObjectMapper();
				config = mapper.readValue(
					inputStream, MicrobotConfig.class
				);
			} catch(java.io.IOException | java.lang.NullPointerException e) {
				onError("Please create 'config/bot.json' file and try again.");
			}
	}
		
	@Override
	public void onUpdateReceived(Update update) {
		
	}
	
	@Override
	public String getBotToken() {
		return config.tg_token;
	}
		
	@Override
	public String getBotUsername() {
		return config.tg_username;
	}
		
	@Override
	public boolean onSuccess(String message) {
		System.out.println(
			SUCCESS_COLOR + "[SUCC] " + RESET_COLOR + message
		);
		return true;
	}
		
	@Override
	public boolean onPadding(String message) {
		System.out.println(
			RESET_COLOR + "       " + message
		);
		return true;
	}
		
	@Override
	public boolean onInfo(String message) {
		System.out.println(
			INFO_COLOR + "[INFO] " + RESET_COLOR + message
		);
		return true;
	}

	@Override
	public boolean onWarning(String message) {
		System.out.println(
			WARNING_COLOR + "[WARN] " + RESET_COLOR + message
		);
		return true;
	}

	@Override
	public boolean onError(String message) {
		System.out.println(
			ERROR_COLOR + "[ERR ] " + RESET_COLOR + message
		);
		return true;
	}
}