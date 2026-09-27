---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the concept of contract and roles that parties to contract play in the context of financial
      agreements. Coverage includes written contracts which are the concrete evidence of agreements between parties and verbal
      contracts. Contracts are further broken down into bilateral and transferable contracts, the latter being the basis for
      most financial instruments, and basic properties of contracts, such as terms and conditions, are also covered.
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
    value: Contracts Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Agreements/Contracts.owl version of the ontology was revised\
      \ in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t\t(1) to use slash style URI/IRIss (also\
      \ called 303 URIs, vs. hash style) as required to support server side processing \n\t\t(2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n\t\t(3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n\t\t(4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t\t(5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250601/Agreements/Contracts.rdf version of this ontology was
      modified to eliminate deprecated constructs that have been deprecated for more than a year (FND-407).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Agreements/Contracts.rdf version of the ontology was
      was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Agreements/Contracts.rdf version of this ontology was
      revised as a part of the issue resolutions identified in the FIBO FND 1.1 RTF report to add a parent of hasDate to date
      properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Agreements/Contracts.rdf version of this ontology was
      revised as a part of the issue resolutions identified in the FIBO FND 1.2 RTF report to revise definitions related to
      contractual element, add contractual commitment and deprecate contract terms set.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20170201/Agreements/Contracts.rdf version of this ontology was
      revised as a part of the issue resolutions identified in the FIBO FND 2.0 RFC to augment restrictions on contract and
      contractual commitment.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Agreements/Contracts.rdf version of this ontology was
      revised to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Agreements/Contracts.rdf version of this ontology was
      revised to add the concept of a term sheet, revise definitions to be ISO 704 compliant, and eliminate duplication of
      concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Agreements/Contracts.rdf version of this ontology was
      revised to add the concepts of breach of contract and breach of covenant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Agreements/Contracts.rdf version of this ontology was
      revised to simplify the contract party hierarchy, eliminate ambiguity in definitions where feasible and add restrictions
      on identity documents to avoid circular dependencies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/Agreements/Contracts.rdf version of this ontology was
      revised to eliminate references to external dictionary sites that no longer resolve, move the concept of an extension
      provision from Debt to Contracts to support representation of preferred shares and other extendable contracts, added
      a property for contract duration which is needed for long-term options, moved PromissoryNote to Debt for better integration
      with related concepts, and integrated additional contractual elements, including representations, warranties, and termination
      provision.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210301/Agreements/Contracts.rdf version of this ontology was
      revised to clean up the definition of transferable contract, including eliminating an unnecessary equivalence, adding
      subclasses for assignable and novatable contracts, and to restrictions from contract to written contract that did not
      make sense with respect to a verbal contract.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/Agreements/Contracts.rdf version of this ontology was
      revised to change a duplicate definition on hasContractDuration to an explanatory note.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210701/Agreements/Contracts.rdf version of this ontology was
      revised to add the concept of a master agreement and fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/Agreements/Contracts.rdf version of this ontology was
      revised to move the property hasTerm from FinancialInstruments to Contracts as it is more broadly applicable.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Agreements/Contracts.rdf version of this ontology was
      revised to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Agreements/Contracts.rdf version of the ontology was
      modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata
      vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Agreements/Contracts.rdf version of this ontology was
      modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating
      redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Agreements/Contracts.rdf version of the ontology was
      modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology
      Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Agreements/Contracts.rdf version of the ontology was
      modified to replace additional concepts from several FIBO FND ontologies with their counterparts added to the Commons
      Ontology Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Agreements/Contracts.rdf version of the ontology was
      modified to better integrate the parties to a contract with the latest patterns (FBC-284).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240501/Agreements/Contracts.rdf version of the ontology was
      modified to add an optional date of issuance to written contract, which may or may not be the same as the effective
      date (FBC-322), to add a general notion of collateral agreement (LOAN-168), and to add provisions for disclosures and
      use of proceeds (LOAN-169).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Agreements/Contracts.rdf version of the ontology was
      modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Agreements/Contracts.rdf version of the ontology was
      modified to link a condition precedent to the contract or clause of a contract on which it depends (DER-55).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250401/Agreements/Contracts.rdf version of the ontology was
      modified to link a beneficiary to the contract to which they are a counterparty, add netting provisions (DER-55a), and
      to eliminate certain constructs that are redundant and will never be materialized to reduce the number of nodes required
      for various contract-related constructs (FND-391).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260601/Agreements/Contracts/
  - concept: /concepts/fibo/FND/AgentsAndPeople/People.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/Agreements/Agreements.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/
  - concept: /concepts/fibo/FND/Arrangements/Documents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
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
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: Contracts Ontology
type: Ontology Definition
---

# Contracts Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/>

## Relationships

- **Related to**: [People](/concepts/fibo/FND/AgentsAndPeople/People.md)
- **Related to**: [Agreements](/concepts/fibo/FND/Agreements/Agreements.md)
- **Related to**: [Documents](/concepts/fibo/FND/Arrangements/Documents.md)
- **Related to**: [FinancialDates](/concepts/fibo/FND/DatesAndTimes/FinancialDates.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
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
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [Contracts](<https://spec.edmcouncil.org/fibo/ontology/FND/20260601/Agreements/Contracts/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the concept of contract and roles that parties to contract play in the context of financial agreements. Coverage includes written contracts which are the concrete evidence of agreements between parties and verbal contracts. Contracts are further broken down into bilateral and transferable contracts, the latter being the basis for most financial instruments, and basic properties of contracts, such as terms and conditions, are also covered.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Contracts Ontology
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Agreements/Contracts.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 		(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  		(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 		(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 		(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 		(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250601/Agreements/Contracts.rdf version of this ontology was modified to eliminate deprecated constructs that have been deprecated for more than a year (FND-407).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Agreements/Contracts.rdf version of the ontology was was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Agreements/Contracts.rdf version of this ontology was revised as a part of the issue resolutions identified in the FIBO FND 1.1 RTF report to add a parent of hasDate to date properties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Agreements/Contracts.rdf version of this ontology was revised as a part of the issue resolutions identified in the FIBO FND 1.2 RTF report to revise definitions related to contractual element, add contractual commitment and deprecate contract terms set.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20170201/Agreements/Contracts.rdf version of this ontology was revised as a part of the issue resolutions identified in the FIBO FND 2.0 RFC to augment restrictions on contract and contractual commitment.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Agreements/Contracts.rdf version of this ontology was revised to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Agreements/Contracts.rdf version of this ontology was revised to add the concept of a term sheet, revise definitions to be ISO 704 compliant, and eliminate duplication of concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Agreements/Contracts.rdf version of this ontology was revised to add the concepts of breach of contract and breach of covenant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200901/Agreements/Contracts.rdf version of this ontology was revised to simplify the contract party hierarchy, eliminate ambiguity in definitions where feasible and add restrictions on identity documents to avoid circular dependencies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201201/Agreements/Contracts.rdf version of this ontology was revised to eliminate references to external dictionary sites that no longer resolve, move the concept of an extension provision from Debt to Contracts to support representation of preferred shares and other extendable contracts, added a property for contract duration which is needed for long-term options, moved PromissoryNote to Debt for better integration with related concepts, and integrated additional contractual elements, including representations, warranties, and termination provision.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210301/Agreements/Contracts.rdf version of this ontology was revised to clean up the definition of transferable contract, including eliminating an unnecessary equivalence, adding subclasses for assignable and novatable contracts, and to restrictions from contract to written contract that did not make sense with respect to a verbal contract.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210401/Agreements/Contracts.rdf version of this ontology was revised to change a duplicate definition on hasContractDuration to an explanatory note.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210701/Agreements/Contracts.rdf version of this ontology was revised to add the concept of a master agreement and fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/Agreements/Contracts.rdf version of this ontology was revised to move the property hasTerm from FinancialInstruments to Contracts as it is more broadly applicable.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Agreements/Contracts.rdf version of this ontology was revised to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Agreements/Contracts.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Agreements/Contracts.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Agreements/Contracts.rdf version of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Agreements/Contracts.rdf version of the ontology was modified to replace additional concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Agreements/Contracts.rdf version of the ontology was modified to better integrate the parties to a contract with the latest patterns (FBC-284).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240501/Agreements/Contracts.rdf version of the ontology was modified to add an optional date of issuance to written contract, which may or may not be the same as the effective date (FBC-322), to add a general notion of collateral agreement (LOAN-168), and to add provisions for disclosures and use of proceeds (LOAN-169).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241101/Agreements/Contracts.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Agreements/Contracts.rdf version of the ontology was modified to link a condition precedent to the contract or clause of a contract on which it depends (DER-55).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250401/Agreements/Contracts.rdf version of the ontology was modified to link a beneficiary to the contract to which they are a counterparty, add netting provisions (DER-55a), and to eliminate certain constructs that are redundant and will never be materialized to reduce the number of nodes required for various contract-related constructs (FND-391).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
