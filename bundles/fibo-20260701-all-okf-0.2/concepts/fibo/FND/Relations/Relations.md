---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines a set of general purpose relations for use in other FIBO ontology elements. These include
      a number of properties required for reuse across the foundations and business entities models.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Relations Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20170201/Relations/Relations.rdf version of this ontology was modified
      per the FIBO 2.0 RFC to include additional properties and the linkage to LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Relations/Relations.owl version of the ontology submitted\
      \ with the FIBO FND RFC, was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t(1)\
      \ to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing\
      \ \n\t(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs\n\t(3)\
      \ to change the file suffix from .owl to .rdf to increase usability in RDF tools\n\t(4) to use 4-level abbreviations\
      \ and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\
      \t(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module,\
      \ and ontology level, similar to the abbreviations\n\t(6) to move the ontology from the Utilities module to an independent\
      \ Relations module\n\t(7) to revise a number of definitions, per discussion with various stakeholders.\n\t(8) to augment\
      \ the definitions to include entity names from Business Entities."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Relations/Relations.rdf version of this ontology was
      revised to add the appliesTo object property in support of the IND RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20140501/Relations/Relations.rdf version of this ontology was
      modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
      It was further revised in FTF 2 resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Relations/Relations/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Relations/Relations.rdf version of this ontology was
      modified per the issue resolutions identified in the FIBO FND 1.2 RTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Relations/Relations.rdf version of this ontology was
      modified to incorporate evaluates and isEvaluatedBy, and to loosen constraints on hasName properties to allow multi-lingual
      names.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190301/Relations/Relations.rdf version of this ontology was
      modified to loosen constraints on properties using xsd:dateTime in their range to allow for more flexible representation,
      and to add properties including produces, isProducedBy.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Relations/Relations.rdf version of this ontology was
      modified to rename (migrate) the hasDefinition property to isDefinedIn.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Relations/Relations.rdf version of this ontology was
      modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Relations/Relations.rdf version of this ontology was
      modified to eliminate duplication with concepts in LCC and remove the unused hasDispositionDate property, whose semantics
      were unclear at best.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Relations/Relations.rdf version of this ontology was
      modified to move hasAcquisitionDate to Financial Dates to improve usability and simplify reasoning, to eliminate circular
      definitions, to deprecate cmns-dsg;hasTag in favor of the simpler LCC property of the same name, to loosen domain restrictions
      on some properties which were too narrowly specified, and to add two new properties, describes and isDescribedBy, which
      are more appropriate for certain cases where we were using characterizes and isCharacterizedBy.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Relations/Relations.rdf version of this ontology was
      modified to move the property 'exchanges' to FND given that it could be applied more generally than with respect to
      swaps only.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/Relations/Relations.rdf version of this ontology was
      modified to clean up references to external dictionaries that don't meet FIBO policies, eliminate ambiguity where possible,
      eliminate the superproperties of produces and is produced by, whose semantics are different from their parent properties,
      and improve ISO 704 compliance of definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Relations/Relations.rdf version of this ontology was
      modified to add Reference as a superclass of Name and use the hasTextValue property as the superproperty of certain
      data properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/Relations/Relations.rdf version of this ontology was
      modified to remove the deprecated hasTag property.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220401/Relations/Relations.rdf version of this ontology was
      modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Relations/Relations.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Relations/Relations.rdf version of this ontology was
      modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology Library
      (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Relations/Relations.rdf version of the ontology was
      modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the
      OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Relations/Relations.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Relations/Relations.rdf version of the ontology was
      modified to eliminate elements that have been deprecated for several quarters (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Relations/Relations.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Relations/Relations.rdf version of the ontology was
      modified to eliminate elements that have been deprecated for more than 3 quarters (FND-399).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Relations/Relations.rdf version of the ontology was
      modified to deprecate duplicate properties, including some that are now available in Commons (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
sources:
- id: fibo-source-5bd2fc8cf9
  resource: references/fibo/FND/Relations/Relations.rdf
  sha256: 5bd2fc8cf9713fc293309a78a9ec760e0eacc6a4c5e9499bbbb29b4f8a172fa2
  title: FIBO source FND/Relations/Relations.rdf
title: Relations Ontology
type: Ontology Definition
---

# Relations Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [Relations](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Relations/Relations/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines a set of general purpose relations for use in other FIBO ontology elements. These include a number of properties required for reuse across the foundations and business entities models.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Relations Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20170201/Relations/Relations.rdf version of this ontology was modified per the FIBO 2.0 RFC to include additional properties and the linkage to LCC.
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Relations/Relations.owl version of the ontology submitted with the FIBO FND RFC, was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 	(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  	(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 	(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 	(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 	(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations 	(6) to move the ontology from the Utilities module to an independent Relations module 	(7) to revise a number of definitions, per discussion with various stakeholders. 	(8) to augment the definitions to include entity names from Business Entities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Relations/Relations.rdf version of this ontology was revised to add the appliesTo object property in support of the IND RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20140501/Relations/Relations.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/. It was further revised in FTF 2 resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Relations/Relations/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Relations/Relations.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.2 RTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Relations/Relations.rdf version of this ontology was modified to incorporate evaluates and isEvaluatedBy, and to loosen constraints on hasName properties to allow multi-lingual names.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190301/Relations/Relations.rdf version of this ontology was modified to loosen constraints on properties using xsd:dateTime in their range to allow for more flexible representation, and to add properties including produces, isProducedBy.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Relations/Relations.rdf version of this ontology was modified to rename (migrate) the hasDefinition property to isDefinedIn.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Relations/Relations.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Relations/Relations.rdf version of this ontology was modified to eliminate duplication with concepts in LCC and remove the unused hasDispositionDate property, whose semantics were unclear at best.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200301/Relations/Relations.rdf version of this ontology was modified to move hasAcquisitionDate to Financial Dates to improve usability and simplify reasoning, to eliminate circular definitions, to deprecate cmns-dsg;hasTag in favor of the simpler LCC property of the same name, to loosen domain restrictions on some properties which were too narrowly specified, and to add two new properties, describes and isDescribedBy, which are more appropriate for certain cases where we were using characterizes and isCharacterizedBy.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Relations/Relations.rdf version of this ontology was modified to move the property 'exchanges' to FND given that it could be applied more generally than with respect to swaps only.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/Relations/Relations.rdf version of this ontology was modified to clean up references to external dictionaries that don't meet FIBO policies, eliminate ambiguity where possible, eliminate the superproperties of produces and is produced by, whose semantics are different from their parent properties, and improve ISO 704 compliance of definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Relations/Relations.rdf version of this ontology was modified to add Reference as a superclass of Name and use the hasTextValue property as the superproperty of certain data properties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/Relations/Relations.rdf version of this ontology was modified to remove the deprecated hasTag property.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220401/Relations/Relations.rdf version of this ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Relations/Relations.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Relations/Relations.rdf version of this ontology was modified to move the property, 'is conferred on' to the Legal Capacity ontology and to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Relations/Relations.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Relations/Relations.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Relations/Relations.rdf version of the ontology was modified to eliminate elements that have been deprecated for several quarters (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Relations/Relations.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Relations/Relations.rdf version of the ontology was modified to eliminate elements that have been deprecated for more than 3 quarters (FND-399).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Relations/Relations.rdf version of the ontology was modified to deprecate duplicate properties, including some that are now available in Commons (FND-412).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
