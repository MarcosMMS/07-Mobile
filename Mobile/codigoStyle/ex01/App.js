import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Component from './components/Componente';
import Styles from './styles/styles'

export default function App(componente) {
  return (
    <View styles={Styles.container}>
        <Component nome="Marcos" />
        <Text style={Styles.Text}> 
          Olá, React Native!!! 
        </Text>
    </View>
  )
}