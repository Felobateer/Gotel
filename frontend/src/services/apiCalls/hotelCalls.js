import axios from 'axios';
import {BASE_URL} from '../constants';

export default class HotelCalls {
    static hotelurl = `${BASE_URL}/hotel`;

    static async getHotelById(hotelId) {
        try {
            const response = await axios.get(`${this.hotelurl}/${hotelId}`);
            return response.data;
        } catch (error) {
            console.error('Error fetching hotel by ID:', error);
            throw error;
        }
    }

    static async getAllHotels() {
        try {
            const response = await axios.get(this.hotelurl);
            return response.data;
        } catch (error) {
            console.error('Error fetching all hotels:', error);
            throw error;
        }
    }

}