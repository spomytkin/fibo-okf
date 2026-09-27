---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the Commons Parties and Situations ontology with identifiers for party roles and very general
      tax identifiers.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\nPermission\
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
    value: Parties Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Parties/Parties.rdf version of the ontology was was modified
      per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Parties/Parties.rdf version of this ontology was revised as
      a part of the issue resolutions identified in the FIBO FND 1.1 RTF report to add a parent of hasDate to date properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20160201/Parties/Parties.rdf version of this ontology was revised as
      a part of the FIBO 2.0 RFC to introduce disjointness axioms to aid users in understanding.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Roles/Parties.owl version of the ontology was revised in\
      \ advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t(1) to use slash style URI/IRIss (also called\
      \ 303 URIs, vs. hash style) as required to support server side processing \n\t(2) to use version-independent IRIs for\
      \ all definitions internally as opposed to version-specific IRIs\n\t(3) to change the file suffix from .owl to .rdf\
      \ to increase usability in RDF tools\n\t(4) to use 4-level abbreviations and corresponding namespace prefixes for all\
      \ FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t(5) to incorporate changes to the\
      \ specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations.\n\t(6) to combine Parties, Party Roles, and Roles in a single, new, Parties module, combine\
      \ Parties and Party Roles into a single ontology, and add an inverse for the hasParty property."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Parties/Parties.rdf version of this ontology was revised
      to add semantics to the definition of independent party, making it a direct subclass of autonomous agent (rather than
      inferred only) and making person and organization direct subclasses (rather than inferred only).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190101/Parties/Parties.rdf version of this ontology was revised
      to add a relationship directly between parties and a party identifier and rename (migrate) the hasDefinition property
      to isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Parties/Parties.rdf version of this ontology was revised
      to eliminate duplication with the concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Parties/Parties.rdf version of this ontology was extended
      to support more complex situations involving parties in various roles, loosen the restriction on party in role with
      respect to commencement date, and to eliminate the redundant union in the definition of independent party.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200601/Parties/Parties.rdf version of this ontology was extended
      to rename 'hasPrimaryParty' to 'hasActiveParty' to be more consistent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Parties/Parties.rdf version of this ontology was extended
      to align the properties holds and isHeldBy with the lattice to improve ownership-related reasoning.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Parties/Parties.rdf version of this ontology was extended
      to add the concepts of tax identifier and tax identification scheme.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201101/Parties/Parties.rdf version of this ontology was revised
      to make hasRelatedPartyInRole symmetric and move hasMailingAddress from people to this ontology.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210301/Parties/Parties.rdf version of this ontology was revised
      to add the two remaining property chains to complete the lattice, from independent party to thing via the situation,
      to simplify the class hierarchy for improved understanding, data mapping and alignment, and to add the notion of a contextual
      name (i.e., a name for someone, some place or something that applies for some period of time in some context).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/Parties/Parties.rdf version of this ontology was revised
      to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Parties/Parties.rdf version of the ontology was modified
      to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Parties/Parties.rdf version of this ontology was modified
      to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Parties/Parties.rdf version of the ontology was modified
      to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Parties/Parties.rdf version of the ontology was modified
      extensively to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Parties/Parties.rdf version of the ontology was modified
      to correct a wrong prefix on hasRole.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240501/Parties/Parties.rdf version of the ontology was modified
      to eliminate elements that have been deprecated for several quarters (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Parties/Parties.rdf version of the ontology was modified
      to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Parties/Parties/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
sources:
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
title: Parties Ontology
type: Ontology Definition
---

# Parties Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/>

## Relationships

- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Parties](<https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Parties/Parties/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the Commons Parties and Situations ontology with identifiers for party roles and very general tax identifiers.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Parties Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Parties/Parties.rdf version of the ontology was was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Parties/Parties.rdf version of this ontology was revised as a part of the issue resolutions identified in the FIBO FND 1.1 RTF report to add a parent of hasDate to date properties.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20160201/Parties/Parties.rdf version of this ontology was revised as a part of the FIBO 2.0 RFC to introduce disjointness axioms to aid users in understanding.
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Roles/Parties.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 	(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  	(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 	(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 	(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 	(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations. 	(6) to combine Parties, Party Roles, and Roles in a single, new, Parties module, combine Parties and Party Roles into a single ontology, and add an inverse for the hasParty property.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Parties/Parties.rdf version of this ontology was revised to add semantics to the definition of independent party, making it a direct subclass of autonomous agent (rather than inferred only) and making person and organization direct subclasses (rather than inferred only).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190101/Parties/Parties.rdf version of this ontology was revised to add a relationship directly between parties and a party identifier and rename (migrate) the hasDefinition property to isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/Parties/Parties.rdf version of this ontology was revised to eliminate duplication with the concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Parties/Parties.rdf version of this ontology was extended to support more complex situations involving parties in various roles, loosen the restriction on party in role with respect to commencement date, and to eliminate the redundant union in the definition of independent party.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200601/Parties/Parties.rdf version of this ontology was extended to rename 'hasPrimaryParty' to 'hasActiveParty' to be more consistent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/Parties/Parties.rdf version of this ontology was extended to align the properties holds and isHeldBy with the lattice to improve ownership-related reasoning.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Parties/Parties.rdf version of this ontology was extended to add the concepts of tax identifier and tax identification scheme.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201101/Parties/Parties.rdf version of this ontology was revised to make hasRelatedPartyInRole symmetric and move hasMailingAddress from people to this ontology.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210301/Parties/Parties.rdf version of this ontology was revised to add the two remaining property chains to complete the lattice, from independent party to thing via the situation, to simplify the class hierarchy for improved understanding, data mapping and alignment, and to add the notion of a contextual name (i.e., a name for someone, some place or something that applies for some period of time in some context).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/Parties/Parties.rdf version of this ontology was revised to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Parties/Parties.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Parties/Parties.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Parties/Parties.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Parties/Parties.rdf version of the ontology was modified extensively to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Parties/Parties.rdf version of the ontology was modified to correct a wrong prefix on hasRole.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240501/Parties/Parties.rdf version of the ontology was modified to eliminate elements that have been deprecated for several quarters (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Parties/Parties.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
