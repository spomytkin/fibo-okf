---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology provides mathematical abstractions for use in other ontologies, including for example the basic components
      of formulae, parameters and values.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Analytics Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20140501/Utilities/Analytics.rdf version of this ontology was
      modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Utilities/Analytics.rdf version of this ontology was
      modified to address issue FIBOFND11-20, which added the definition of Calculation and corrected a reasoning issue related
      to the use of a custom datatype.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Utilities/Analytics.rdf version of this ontology was
      modified per the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Utilities/Analytics.rdf version of this ontology was
      modified to use the CombinedDateTime datatype for greater flexibility in analytics and integrate the generic statistical
      measures and measurements from the economic indicators ontology to FND to facilitate broader use.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Utilities/Analytics.rdf version of this ontology was
      modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Utilities/Analytics.rdf version of this ontology was
      modified to add the concept of a weighting algorithm.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20191101/Utilities/Analytics.rdf version of this ontology was
      modified to eliminate duplication with concepts in LCC, merge countries with locations, and correct a restriction on
      qualified measure.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Utilities/Analytics.rdf version of this ontology was
      modified to revise numeric index to be called numeric index value, and revise its definition to include a reference
      date, change its parent to quantity value, and move base date and period to scoped measure.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200401/Utilities/Analytics.rdf version of this ontology was
      modified to change the parent class of Classifier to Aspect, loosen the domain on the hasArgument property, which was
      too narrow in some cases, add a domain/range to characterizes/isCharacterizedBy, and eliminate duplicate properties
      that were not used anywhere.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Utilities/Analytics.rdf version of this ontology was
      modified to augment the definition of ratio with a synonym of rate and eliminate the circularity in the definition of
      standard deviation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Utilities/Analytics.rdf version of this ontology was
      modified to make statistical program a subclass of program and revised restrictions on statistical program to better
      reflect its intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201101/Utilities/Analytics.rdf version of this ontology was
      modified to eliminate the redundant 'calculation formula' concept and eliminate the property hasOperand, which is not
      used anywhere and whose definition is circular.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Utilities/Analytics.rdf version of this ontology was
      modified to update the reference link for ratio.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/Utilities/Analytics.rdf version of this ontology was
      modified to expand the definition of release date and release date and time and to make a statistical area identifier
      a subclass of geographic region identifier.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211101/Utilities/Analytics.rdf version of this ontology was
      modified to eliminate unused imports.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Utilities/Analytics.rdf version of this ontology was
      modified to eliminate hygiene issues related to text formatting and eliminate dead or outdated references.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Utilities/Analytics.rdf version of this ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Utilities/Analytics.rdf version of this ontology was
      modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Utilities/Analytics.rdf version of this ontology was
      modified to add a synonym of 'average' to arithmetic mean.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230501/Utilities/Analytics.rdf version of the ontology was
      modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Utilities/Analytics.rdf version of the ontology was
      modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Utilities/Analytics.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380)
      and to move the concept of an anchor date to Financial Dates (FBC-317).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240201/Utilities/Analytics.rdf version of the ontology was
      modified to eliminate elements that have been deprecated for several quarters (FND-386) and to add the concept of a
      key performance indicator (KPI) (LOAN-169).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Utilities/Analytics.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: This ontology was added to Foundations in advance of the June 2014 Boston meeting in support of the IND RFC.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Utilities/Analytics/
  - concept: /concepts/fibo/FND/Arrangements/Arrangements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Arrangements/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/
sources:
- id: fibo-source-9af4d662d7
  resource: references/fibo/FND/Utilities/Analytics.rdf
  sha256: 9af4d662d742fca95008743be6787bb2bd1fbfc7f881b5273e0e74b1b60ba5fb
  title: FIBO source FND/Utilities/Analytics.rdf
title: Analytics Ontology
type: Ontology Definition
---

# Analytics Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/>

## Relationships

- **Related to**: [Arrangements](/concepts/fibo/FND/Arrangements/Arrangements.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [Analytics](<https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Utilities/Analytics/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology provides mathematical abstractions for use in other ontologies, including for example the basic components of formulae, parameters and values.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Analytics Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20140501/Utilities/Analytics.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Utilities/Analytics.rdf version of this ontology was modified to address issue FIBOFND11-20, which added the definition of Calculation and corrected a reasoning issue related to the use of a custom datatype.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Utilities/Analytics.rdf version of this ontology was modified per the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Utilities/Analytics.rdf version of this ontology was modified to use the CombinedDateTime datatype for greater flexibility in analytics and integrate the generic statistical measures and measurements from the economic indicators ontology to FND to facilitate broader use.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Utilities/Analytics.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Utilities/Analytics.rdf version of this ontology was modified to add the concept of a weighting algorithm.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20191101/Utilities/Analytics.rdf version of this ontology was modified to eliminate duplication with concepts in LCC, merge countries with locations, and correct a restriction on qualified measure.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Utilities/Analytics.rdf version of this ontology was modified to revise numeric index to be called numeric index value, and revise its definition to include a reference date, change its parent to quantity value, and move base date and period to scoped measure.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200401/Utilities/Analytics.rdf version of this ontology was modified to change the parent class of Classifier to Aspect, loosen the domain on the hasArgument property, which was too narrow in some cases, add a domain/range to characterizes/isCharacterizedBy, and eliminate duplicate properties that were not used anywhere.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Utilities/Analytics.rdf version of this ontology was modified to augment the definition of ratio with a synonym of rate and eliminate the circularity in the definition of standard deviation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Utilities/Analytics.rdf version of this ontology was modified to make statistical program a subclass of program and revised restrictions on statistical program to better reflect its intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201101/Utilities/Analytics.rdf version of this ontology was modified to eliminate the redundant 'calculation formula' concept and eliminate the property hasOperand, which is not used anywhere and whose definition is circular.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Utilities/Analytics.rdf version of this ontology was modified to update the reference link for ratio.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/Utilities/Analytics.rdf version of this ontology was modified to expand the definition of release date and release date and time and to make a statistical area identifier a subclass of geographic region identifier.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211101/Utilities/Analytics.rdf version of this ontology was modified to eliminate unused imports.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Utilities/Analytics.rdf version of this ontology was modified to eliminate hygiene issues related to text formatting and eliminate dead or outdated references.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Utilities/Analytics.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Utilities/Analytics.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Utilities/Analytics.rdf version of this ontology was modified to add a synonym of 'average' to arithmetic mean.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230501/Utilities/Analytics.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Utilities/Analytics.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Utilities/Analytics.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380) and to move the concept of an anchor date to Financial Dates (FBC-317).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240201/Utilities/Analytics.rdf version of the ontology was modified to eliminate elements that have been deprecated for several quarters (FND-386) and to add the concept of a key performance indicator (KPI) (LOAN-169).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Utilities/Analytics.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: This ontology was added to Foundations in advance of the June 2014 Boston meeting in support of the IND RFC.
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
