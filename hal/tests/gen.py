import os

from hal.meta.attributes import get_modules, ModuleFile, MODULE_SEP

DOCS = "\"\"\"{}\"\"\""
TODO = "# todo auto generated method stub"
INDENTATION = "    "
CLASS_KEYWORD = "class"
METHOD_KEYWORD = "def"


class TestWriter:
    """Auto-generates test methods stubs for module"""

    def __init__(self, root_folder):
        """
        :param root_folder: folder of root module
        """

        self.root_folder = root_folder
        self.modules = self._get_modules()

    def _get_modules(self):
        """Finds modules in root folder

        :return: list of modules
        """

        modules = get_modules(self.root_folder, include_meta=False)
        modules = [
            ModuleFile(mod, self.root_folder)
            for mod in modules
        ]
        return modules

    @staticmethod
    def get_imports(to_import):
        """Auto generates imports

        :param to_import: list of modules to import
        :return: list of imports
        """

        return [
            "from " + item.package + " import " + item.get_name()
            for item in to_import
        ]

    @staticmethod
    def get_functions_tests(functions, indent=0, static=False):
        """Auto generates functions tests

        :param functions: list of functions
        :param indent: indentation level
        :param static: whether is a static method or not
        :return: list of tests
        """

        tests = []
        start_indent = indent * INDENTATION
        inner_indent = (indent + 1) * INDENTATION
        new_line = "\n" + inner_indent

        for func in functions:
            name = "test_" + func.get_name()
            signature = METHOD_KEYWORD + " " + name + "():"
            content = "pass  " + TODO
            docs = DOCS.format("Tests " + func.full_package + " method")

            if static:
                test = start_indent + "@staticmethod" + "\n"
            else:
                test = ""

            test += start_indent + signature
            test += new_line + docs
            test += "\n" + new_line + content

            tests.append(test)

        return tests

    @staticmethod
    def get_classes_tests(classes, indent=0):
        """Auto generates classes tests

        :param classes: list of classes
        :param indent: indentation level
        :return: list of tests
        """

        tests = []
        start_indent = indent * INDENTATION
        inner_indent = (indent + 1) * INDENTATION
        new_line = "\n" + inner_indent

        for cl in classes:
            name = "Test" + cl.get_name()
            signature = CLASS_KEYWORD + " " + name + ":"
            cl_docs = DOCS.format("Tests " + cl.get_name() + " class")
            functions = cl.get_functions()

            if functions:
                content = "\n\n".join(
                    TestWriter.get_functions_tests(functions, indent + 1, True)
                )
            else:
                content = inner_indent + "pass  " + TODO

            test = start_indent + signature
            test += new_line + cl_docs
            test += "\n\n" + content

            tests.append(test)

        return tests

    @staticmethod
    def get_module_tests(mod):
        """Auto generates module tests

        :param mod: path to source of module
        :return: tests for module
        """

        functions = mod.get_tree().get_functions()
        classes = mod.get_tree().get_classes()

        header = "# -*- coding: utf-8 -*-"
        docs = DOCS.format("Tests " + mod.package + " implementation")
        imports = "\n".join(
            TestWriter.get_imports(functions) + TestWriter.get_imports(classes)
        )
        tests = "\n\n\n".join(
            TestWriter.get_functions_tests(functions) +
            TestWriter.get_classes_tests(classes)
        )

        contents = header + "\n\n\n" + docs + "\n\n" + imports
        contents += "\n\n\n" + tests

        return contents + "\n"  # PEP 8: no newline at end of file

    def write_tests(self, output_folder):
        """Writes test stubs for modules in folder

        :param output_folder: output folder
        """

        if not os.path.exists(output_folder):  # prepare necessary folders
            os.makedirs(output_folder)

        for mod in self.modules:
            file_name = mod.package.replace(MODULE_SEP, "_")
            file_name = "test_" + file_name + ".py"
            output_file = os.path.join(output_folder, file_name)

            with open(output_file, "w") as writer:
                contents = self.get_module_tests(mod)
                writer.write(contents)
