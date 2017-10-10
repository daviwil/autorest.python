﻿// This file is used by Code Analysis to maintain SuppressMessage 
// attributes that are applied to this project.
// Project-level suppressions either have no target or are given 
// a specific target and scoped to a namespace, type, member, etc.
//
// To add a suppression to this file, right-click the message in the 
// Code Analysis results, point to "Suppress Message", and click 
// "In Suppression File".
// You do not need to add suppressions to this file manually.

[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1002:DoNotExposeGenericLists", Scope = "member", 
    Target = "AutoRest.Python.ServiceClientTemplateModel.#ModelTemplateModels", Justification="Using another type would add unneeded complexity")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1002:DoNotExposeGenericLists", Scope = "member", 
    Target = "AutoRest.Python.MethodGroupTemplateModel.#MethodTemplateModels", Justification="Using another type would add unneeded complexity")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1002:DoNotExposeGenericLists", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#ParameterTemplateModels", Justification="Using another type would add unneeded complexity")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1002:DoNotExposeGenericLists", Scope = "member", 
    Target = "AutoRest.Python.ServiceClientTemplateModel.#MethodTemplateModels", Justification="Using another type would add unneeded complexity")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1020:AvoidNamespacesWithFewTypes", 
    Scope = "namespace", Target = "AutoRest.Python.TemplateModels", Justification = "Parallel with other generators")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", 
    Scope = "member", 
    Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String)", Justification="Code simplification")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", 
    Scope = "member", 
    Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#DeserializeType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String)", Justification="Code simplification")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", 
    Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#GetDeserializationString(AutoRest.Core.ClientModel.IType,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1054:UriParametersShouldNotBeStrings", 
    MessageId = "0#", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#RemoveDuplicateForwardSlashes(System.String)", Justification="Uri will not pass uri validation")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1055:UriReturnValuesShouldNotBeStrings", 
    Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#BuildUrl(System.String)", Justification="Uri will not pass uri validation")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1062:Validate arguments of public methods", 
    MessageId = "1", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#.ctor(AutoRest.Core.ClientModel.Method,AutoRest.Core.ClientModel.ServiceClient)", Justification="Validated by LoadFrom method")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1062:Validate arguments of public methods", 
    MessageId = "0", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#.ctor(AutoRest.Core.ClientModel.Method,AutoRest.Core.ClientModel.ServiceClient)", Justification="Validated by LoadFrom method")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1062:Validate arguments of public methods", 
    MessageId = "0", Scope = "member", 
    Target = "AutoRest.Python.ModelTemplateModel.#.ctor(AutoRest.Core.ClientModel.CompositeType,AutoRest.Core.ClientModel.ServiceClient)", Justification="Validated by LoadFrom method")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#DeserializeType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String)", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateRequiredType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String)", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String)", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#GetDeserializationString(AutoRest.Core.ClientModel.IType,System.String)", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.ServiceClientTemplateModel.#PolymorphicDictionary", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#BuildUrl(System.String)", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", 
    "CA1303:Do not pass literals as localized parameters", 
    MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", 
    Target = "AutoRest.Python.MethodTemplateModel.#RemoveDuplicateForwardSlashes(System.String)", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.ServiceClientTemplateModel.#PolymorphicDictionary", Justification="Literal string is generated code, no localization concerns")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", 
    Scope = "member", 
    Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String)", Justification="Node conventions require lower casing")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily", 
    Scope = "member", 
    Target = "AutoRest.Python.ModelTemplateModel.#isSpecial(AutoRest.Core.ClientModel.IType)", Justification="False Positive")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", 
    MessageId = "gi", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#RemoveDuplicateForwardSlashes(System.String)", Justification="Generated code parameters to regular expression")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#AddQueryParametersToUrl(System.String,AutoRest.Core.Utilities.IndentedStringBuilder)", Justification="Literal string is generated code, no localization concerns.")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#BuildQueryParameterArray(AutoRest.Core.Utilities.IndentedStringBuilder)", Justification="Literal string is generated code, no localization concerns.")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1702:CompoundWordsShouldBeCasedCorrectly", MessageId = "QueryParameters", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#HasQueryParameters()", Justification="False Positive")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1703:ResourceStringsShouldBeSpelledCorrectly", MessageId = "ms-rest", Scope = "resource", Target = "AutoRest.Python.Properties.Resources.resources", Justification="ms-rest is a valid npm package name")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "isArray", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "util", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "isDuration", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ConstructValidationCheck(System.String,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ConstructValidationCheck(System.String,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "instanceof", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "valueOf", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "typeof", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateDictionaryType(AutoRest.Core.ClientModel.DictionaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateDictionaryType(AutoRest.Core.ClientModel.DictionaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateSequenceType(AutoRest.Core.ClientModel.SequenceType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateSequenceType(AutoRest.Core.ClientModel.SequenceType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateCompositeType(AutoRest.Core.ClientModel.CompositeType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateCompositeType(AutoRest.Core.ClientModel.CompositeType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateEnumType(AutoRest.Core.ClientModel.EnumType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateEnumType(AutoRest.Core.ClientModel.EnumType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "isNaN", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "isNaN", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "valueOf", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "typeof", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "instanceof", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateEnumType(AutoRest.Core.ClientModel.EnumType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateEnumType(AutoRest.Core.ClientModel.EnumType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ConstructValidationCheck(AutoRest.Core.Utilities.IndentedStringBuilder,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ConstructValidationCheck(AutoRest.Core.Utilities.IndentedStringBuilder,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidatePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializePrimaryType(AutoRest.Core.ClientModel.PrimaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ConstructBasePropertyCheck(AutoRest.Core.Utilities.IndentedStringBuilder,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeEnumType(AutoRest.Core.ClientModel.EnumType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeEnumType(AutoRest.Core.ClientModel.EnumType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeCompositeType(AutoRest.Core.ClientModel.CompositeType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.Append(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeCompositeType(AutoRest.Core.ClientModel.CompositeType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeSequenceType(AutoRest.Core.ClientModel.SequenceType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeDictionaryType(AutoRest.Core.ClientModel.DictionaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeDictionaryType(AutoRest.Core.ClientModel.DictionaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#DeserializeType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#DeserializeType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#InitializeType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#InitializeSerializationType(AutoRest.Core.ClientModel.IType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ProcessBasicType(System.String,System.String,AutoRest.Core.Utilities.IndentedStringBuilder)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ProcessCompositeType(AutoRest.Core.ClientModel.CompositeType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String,AutoRest.Core.Utilities.IndentedStringBuilder,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ProcessSequenceType(AutoRest.Core.ClientModel.SequenceType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String,AutoRest.Core.Utilities.IndentedStringBuilder,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ProcessDictionaryType(AutoRest.Core.ClientModel.DictionaryType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.String,AutoRest.Core.Utilities.IndentedStringBuilder,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#InitializeResponseBody(AutoRest.Core.ClientModel.IType)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#ConstructParameterDocumentation(System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#GetDeserializationString(AutoRest.Core.ClientModel.IType,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#GetDeserializationString(AutoRest.Core.ClientModel.IType,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#GetValidationString()")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1026:DefaultParametersShouldNotBeUsed", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#DeserializeResponse(AutoRest.Core.ClientModel.IType,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#DeserializeResponse(AutoRest.Core.ClientModel.IType,System.String,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.ModelTemplateModel.#ConstructPropertyDocumentation(System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#SerializeSequenceType(AutoRest.Core.ClientModel.SequenceType,AutoRest.Core.Utilities.IScopeProvider,System.String,System.String,System.Boolean,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ProcessCompositeType(AutoRest.Core.ClientModel.CompositeType,System.String,System.String,System.String,AutoRest.Core.Utilities.IndentedStringBuilder,System.String)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.MethodTemplateModel.#ValidationString")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)", Scope = "member", Target = "AutoRest.Python.TemplateModels.ClientModelExtensions.#ValidateCompositeType(AutoRest.Core.Utilities.IScopeProvider,System.String,System.Boolean)")]
[assembly: System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode", Scope = "member", Target = "AutoRest.Python.ModelTemplateModel.#isSpecial(AutoRest.Core.ClientModel.IType)")]
