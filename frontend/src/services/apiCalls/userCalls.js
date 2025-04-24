import axios from "axios";
import { BASE_URL } from "../constants";
import { vuex } from 'vuex';

export default class UserCalls {
    static userurl = `${BASE_URL}/user`;

    static async getUserById(userId) {
        try {
            const response = await axios.get(`${this.userurl}/${userId}`);
            return response.data;
        } catch (error) {
            console.error("Error fetching user by ID:", error);
            throw error;
        }
    }

    static async signup(userData) {
        try {
            const response = await axios.post(`${this.userurl}/signup`, userData);
            return response.data;
        } catch (error) {
            console.error("Error signing up user:", error);
            throw error;
        }
    }

    static async login(userData) {
        try {
            const response = await axios.post(`${this.userurl}/login`, userData);
            const { token, userId } = response.data;
            vuex.commit('setUser', { token, userId });
            return response.data;
        } catch (error) {
            console.error("Error logging in user:", error);
            throw error;
        }
    }

    static async updateUser(userId, userData) {
        try {
            const response = await axios.put(`${this.userurl}/${userId}`, userData);
            return response.data;
        } catch (error) {
            console.error("Error updating user:", error);
            throw error;
        }
    }

    static async deleteUser(userId) {
        try {
            const response = await axios.delete(`${this.userurl}/${userId}`);
            return response.data;
        } catch (error) {
            console.error("Error deleting user:", error);
            throw error;
        }
    }

    static async forgotPassword(email) {
        try {
            const response = await axios.post(`${this.userurl}/forgot-password`, { email });
            return response.data;
        } catch (error) {
            console.error("Error sending forgot password email:", error);
            throw error;
        }
    }

    static async resetPassword(token, newPassword) {
        try {
            const response = await axios.post(`${this.userurl}/reset-password`, { token, newPassword });
            return response.data;
        } catch (error) {
            console.error("Error resetting password:", error);
            throw error;
        }
    }
}