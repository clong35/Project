import 'package:flutter/material.dart';
import 'package:flutter_form_builder/flutter_form_builder.dart';
import 'package:form_builder_validators/form_builder_validators.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Machine Learning Project',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Data Training Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final _formKey = GlobalKey<FormBuilderState>();
  // String _selectedModel = "Linear Regression";


  void _onChanged(dynamic val) => debugPrint(val.toString());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            FormBuilder(
              onChanged: () {
                _formKey.currentState!.save();
                debugPrint(_formKey.currentState!.value.toString());
              },
              key: _formKey,
              child: Column(
                children: [
                  FormBuilderFilterChip<String>(
                    decoration: const InputDecoration(labelText: "Selected features"),
                    spacing: 10,
                    options: const [
                      "Hello",
                      "World",
                    ]
                        .map((lang) => FormBuilderChipOption(
                              value: lang,
                              child: Tooltip(
                                message: "Testing",
                                child: Text(lang),
                              ),
                            ))
                        .toList(growable: false),
                    // validator: FormBuilderValidators.compose(
                    //     [FormBuilderValidators.min(1)]),
                    name: 'selectedFeatures',
                    onChanged: _onChanged,
                  ),
                ],
              ),
            ),
            FormBuilderChoiceChip(
              autovalidateMode: AutovalidateMode.onUserInteraction,
              decoration: const InputDecoration(labelText: "Select model to train"),
              initialValue: "Linear Regression",
              spacing: 10,
              name: "selectedModel",
              options: ["Linear Regression", "Decision Tree", "Random Forest"]
                  .map((lang) => FormBuilderChipOption(
                        value: lang,
                        child: Text(lang),
                      ))
                  .toList(growable: false),
              // validator:
              //     FormBuilderValidators.compose([FormBuilderValidators.min(1)]),
              onChanged: _onChanged,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          if (_formKey.currentState?.saveAndValidate() ?? false) {
            debugPrint(_formKey.currentState?.value.toString());
          } else {
            debugPrint(_formKey.currentState?.value.toString());
            debugPrint('validation failed');
          }
        },
        tooltip: 'Train Model',
        child: const Text("Train"),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
