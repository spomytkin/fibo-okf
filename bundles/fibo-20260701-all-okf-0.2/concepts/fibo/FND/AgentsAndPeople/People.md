---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts for people and human related terms, for use in other FIBO ontology elements. People
      as defined here are human persons only. This ontology sets out a number of basic properties which are held by people
      or are definitive of a small number of specific types of people such as minors or adults. Primary use cases for determining
      the set of personal information definitions included are the common elements required to (1) open a bank account, (2)
      identify a sophisticated investor, and (3) establish foreign account ownership for money laundering purposes.
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
    value: People Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://spec.edmcouncil.org/fibo/ontology/FND/20130801/AgentsAndPeople/People.rdf version of the ontology was
      was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
      It was further revised in the FTF in advance of the Long Beach meeting, resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/AgentsAndPeople/People/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://spec.edmcouncil.org/fibo/ontology/FND/20141101/AgentsAndPeople/People.rdf version of the ontology was
      was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report, primarily to use the hasAddress property
      in addresses, and change PostalAddress to PhysicalAddress in a restriction on Person. Also revised the identifiesAddress
      property in favor of verifiesAddress, and revised hasDateofBirth with respect to an identity document to be verifiesDateOfBirth,
      which was determined to be more appropriate by the RTF.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/AgentsAndPeople/People.owl version of the ontology was revised\
      \ in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t\t(1) to use slash style URI/IRIss (also\
      \ called 303 URIs, vs. hash style) as required to support server side processing \n\t\t(2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n\t\t(3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n\t\t(4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t\t(5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations.\n\t\t(6) to revise and extend the set of properties about people required to fulfill the set\
      \ of use cases listed above."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/AgentsAndPeople/People.rdf version of the ontology was
      modified per the FIBO 2.0 RFC, including integration of LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/AgentsAndPeople/People.rdf version of the ontology was
      modified to deprecate legally capable person in favor of natural person (defined in Business Entities).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20181101/AgentsAndPeople/People.rdf version of the ontology was
      was modified to revise a restriction on IdentityDocument to reference the appropriate identifier rather than use a tag.
      The impetus behind this change is to support privacy legislation, such as GDPR, which requires protection of both identifiers,
      such as a passport number, drivers' license number, etc. as well as the documents themselves. Thus, properties and individuals
      related to those identifiers are urgently needed.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/AgentsAndPeople/People.rdf version of the ontology was
      modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/AgentsAndPeople/People.rdf version of the ontology was
      modified to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/AgentsAndPeople/People.rdf version of the ontology was
      modified to eliminate duplication with concepts in LCC and correct a bug in a restriction on identity document.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/AgentsAndPeople/People.rdf version of the ontology was
      modified to add explicit DateOfBirth and DateOfDeath, added DeathCertificate and related concepts, streamlined related
      properties and restrictions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/AgentsAndPeople/People.rdf version of the ontology was
      modified to add hasResidence, hasMailingAddress, and hasPrimaryResidence properties and a restriction on person with
      respect to residence accordingly, then to move hasMailingAddress to Parties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210301/AgentsAndPeople/People.rdf version of the ontology was
      modified to allow the People ontology to import Parties, rather than the other way around, to simplify the class hierarchy
      for ease of use in data mapping and alignment, and to add person name as a first class concept, revising property definitions
      to allow for structured names by loosening constraints.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/AgentsAndPeople/People.rdf version of the ontology was
      modified to add concepts specific to legal age, age of majority, legal working age and legal working age person.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/AgentsAndPeople/People.rdf version of the ontology was
      modified to revise the definition of passport number as a national identification number and eliminate restrictions
      that would cause people to be inferred to be passports.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211101/AgentsAndPeople/People.rdf version of the ontology was
      modified to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/AgentsAndPeople/People.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/AgentsAndPeople/People.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC)
      and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/AgentsAndPeople/People.rdf version of the ontology was
      modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology
      Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/AgentsAndPeople/People.rdf version of the ontology was
      modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/AgentsAndPeople/People.rdf version of the ontology was
      modified to replace an additional property with its equivalent from the OMG Commons Ontology Library (Commons) v1.1
      (FBC-322).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/AgentsAndPeople/People.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/AgentsAndPeople/People.rdf version of the ontology was
      modified to add the concept of a contact, as a role someone can play, and of contact record, as the representation of
      the details that store the relevant information (FND-397).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250901/AgentsAndPeople/People.rdf version of the ontology was
      modified to deprecate duplicate properties that are now available in OMG Commons Ontology Library (Commons) v1.3 (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/Arrangements/Documents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/
  - concept: /concepts/fibo/FND/Arrangements/IdentifiersAndIndices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/Parties/Parties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
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
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: People Ontology
type: Ontology Definition
---

# People Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/>

## Relationships

- **Related to**: [Documents](/concepts/fibo/FND/Arrangements/Documents.md)
- **Related to**: [IdentifiersAndIndices](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Parties](/concepts/fibo/FND/Parties/Parties.md)
- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [People](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/AgentsAndPeople/People/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts for people and human related terms, for use in other FIBO ontology elements. People as defined here are human persons only. This ontology sets out a number of basic properties which are held by people or are definitive of a small number of specific types of people such as minors or adults. Primary use cases for determining the set of personal information definitions included are the common elements required to (1) open a bank account, (2) identify a sophisticated investor, and (3) establish foreign account ownership for money laundering purposes.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: People Ontology
- **changeNote**: The http://spec.edmcouncil.org/fibo/ontology/FND/20130801/AgentsAndPeople/People.rdf version of the ontology was was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/. It was further revised in the FTF in advance of the Long Beach meeting, resulting in https://spec.edmcouncil.org/fibo/ontology/FND/20141101/AgentsAndPeople/People/.
- **changeNote**: The http://spec.edmcouncil.org/fibo/ontology/FND/20141101/AgentsAndPeople/People.rdf version of the ontology was was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report, primarily to use the hasAddress property in addresses, and change PostalAddress to PhysicalAddress in a restriction on Person. Also revised the identifiesAddress property in favor of verifiesAddress, and revised hasDateofBirth with respect to an identity document to be verifiesDateOfBirth, which was determined to be more appropriate by the RTF.
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/AgentsAndPeople/People.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 		(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  		(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 		(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 		(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 		(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations. 		(6) to revise and extend the set of properties about people required to fulfill the set of use cases listed above.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/AgentsAndPeople/People.rdf version of the ontology was modified per the FIBO 2.0 RFC, including integration of LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/AgentsAndPeople/People.rdf version of the ontology was modified to deprecate legally capable person in favor of natural person (defined in Business Entities).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20181101/AgentsAndPeople/People.rdf version of the ontology was was modified to revise a restriction on IdentityDocument to reference the appropriate identifier rather than use a tag. The impetus behind this change is to support privacy legislation, such as GDPR, which requires protection of both identifiers, such as a passport number, drivers' license number, etc. as well as the documents themselves. Thus, properties and individuals related to those identifiers are urgently needed.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/AgentsAndPeople/People.rdf version of the ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/AgentsAndPeople/People.rdf version of the ontology was modified to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/AgentsAndPeople/People.rdf version of the ontology was modified to eliminate duplication with concepts in LCC and correct a bug in a restriction on identity document.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/AgentsAndPeople/People.rdf version of the ontology was modified to add explicit DateOfBirth and DateOfDeath, added DeathCertificate and related concepts, streamlined related properties and restrictions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/AgentsAndPeople/People.rdf version of the ontology was modified to add hasResidence, hasMailingAddress, and hasPrimaryResidence properties and a restriction on person with respect to residence accordingly, then to move hasMailingAddress to Parties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210301/AgentsAndPeople/People.rdf version of the ontology was modified to allow the People ontology to import Parties, rather than the other way around, to simplify the class hierarchy for ease of use in data mapping and alignment, and to add person name as a first class concept, revising property definitions to allow for structured names by loosening constraints.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/AgentsAndPeople/People.rdf version of the ontology was modified to add concepts specific to legal age, age of majority, legal working age and legal working age person.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210601/AgentsAndPeople/People.rdf version of the ontology was modified to revise the definition of passport number as a national identification number and eliminate restrictions that would cause people to be inferred to be passports.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211101/AgentsAndPeople/People.rdf version of the ontology was modified to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/AgentsAndPeople/People.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/AgentsAndPeople/People.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/AgentsAndPeople/People.rdf version of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/AgentsAndPeople/People.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/AgentsAndPeople/People.rdf version of the ontology was modified to replace an additional property with its equivalent from the OMG Commons Ontology Library (Commons) v1.1 (FBC-322).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/AgentsAndPeople/People.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/AgentsAndPeople/People.rdf version of the ontology was modified to add the concept of a contact, as a role someone can play, and of contact record, as the representation of the details that store the relevant information (FND-397).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250901/AgentsAndPeople/People.rdf version of the ontology was modified to deprecate duplicate properties that are now available in OMG Commons Ontology Library (Commons) v1.3 (FND-412).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
