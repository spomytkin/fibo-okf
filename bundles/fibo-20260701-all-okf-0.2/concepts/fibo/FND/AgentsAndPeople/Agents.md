---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the Commons 1.1 Parties and Situations ontology to define defines the concept of a software
      system, which may or may not be autonomous. Other concepts that were originally defined in this ontology have been replaced
      with their corresponding concepts in Commons.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\n\t\tCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\n\t\
      \tPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Agents Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/AgentsAndPeople/Agents.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to support the FIBO 2.0 RFC, primarily with respect to equivalence relationships to LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to loosen the range restriction on hasName to rdfs:Literal, facilitating multi-lingual name representation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190301/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to eliminate duplication with concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to add a custom datatype for text values (which might be either xsd:string or rdf:langString) and use that
      in the restriction on hasName on autonomous agent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to add notes on the custom Text datatype indicating that it is outside the RL profile and that if someone
      wants to use this ontology with OWL 2 RL rules they might want to comment this out / eliminate it where it is used.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210901/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/AgentsAndPeople/Agents.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC)
      and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/AgentsAndPeople/Agents.rdf version of the ontology was
      modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/AgentsAndPeople/Agents.rdf version of the ontology was
      modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/AgentsAndPeople/Agents.rdf version of the ontology was
      modified to eliminate elements that have been deprecated for several quarters (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/AgentsAndPeople/Agents.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/AgentsAndPeople/Agents.rdf version of the ontology was
      modified to deprecate the concept of automated system, since it is only used in one place and is not well defined, thus
      allowing elimination of this ontology to simplify FND for better usability (FND-411).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The https://spec.edmcouncil.org/fibo/ontology/Foundations/20130601/AgentsAndPeople/Agents.owl version of the ontology\
      \ was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t\t(1) to use slash style URI/IRIs\
      \ (also called 303 URIs, vs. hash style) as required to support server side processing \n\t\t(2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n\t\t(3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n\t\t(4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t\t(5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations."
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/AgentsAndPeople/Agents/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/Agents/
sources:
- id: fibo-source-324abaa4df
  resource: references/fibo/FND/AgentsAndPeople/Agents.rdf
  sha256: 324abaa4df302ba2a4ce097de0ff752a9da0261301868faf9b36c7cc4577e4af
  title: FIBO source FND/AgentsAndPeople/Agents.rdf
title: Agents Ontology
type: Ontology Definition
---

# Agents Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/Agents/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Agents](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/AgentsAndPeople/Agents/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the Commons 1.1 Parties and Situations ontology to define defines the concept of a software system, which may or may not be autonomous. Other concepts that were originally defined in this ontology have been replaced with their corresponding concepts in Commons.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. 		Copyright (c) 2013-2025 Object Management Group, Inc. 		 		Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Agents Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/AgentsAndPeople/Agents.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/AgentsAndPeople/Agents.rdf version of this ontology was modified to support the FIBO 2.0 RFC, primarily with respect to equivalence relationships to LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/AgentsAndPeople/Agents.rdf version of this ontology was modified to loosen the range restriction on hasName to rdfs:Literal, facilitating multi-lingual name representation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190301/AgentsAndPeople/Agents.rdf version of this ontology was modified to eliminate duplication with concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/AgentsAndPeople/Agents.rdf version of this ontology was modified to add a custom datatype for text values (which might be either xsd:string or rdf:langString) and use that in the restriction on hasName on autonomous agent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/AgentsAndPeople/Agents.rdf version of this ontology was modified to add notes on the custom Text datatype indicating that it is outside the RL profile and that if someone wants to use this ontology with OWL 2 RL rules they might want to comment this out / eliminate it where it is used.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210901/AgentsAndPeople/Agents.rdf version of this ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/AgentsAndPeople/Agents.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/AgentsAndPeople/Agents.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/AgentsAndPeople/Agents.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/AgentsAndPeople/Agents.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/AgentsAndPeople/Agents.rdf version of the ontology was modified to eliminate elements that have been deprecated for several quarters (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/AgentsAndPeople/Agents.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/AgentsAndPeople/Agents.rdf version of the ontology was modified to deprecate the concept of automated system, since it is only used in one place and is not well defined, thus allowing elimination of this ontology to simplify FND for better usability (FND-411).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/Foundations/20130601/AgentsAndPeople/Agents.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 		(1) to use slash style URI/IRIs (also called 303 URIs, vs. hash style) as required to support server side processing  		(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 		(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 		(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 		(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
